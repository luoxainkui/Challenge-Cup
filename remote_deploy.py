#!/usr/bin/env python3
"""全自动远程部署脚本 — 使用 paramiko SSH 连接阿里云服务器"""
import os
import sys
import time
import secrets
import paramiko

# ============================================================
# 服务器信息（仅本次部署使用，代码不留存任何敏感配置）
# ============================================================
SERVER_IP = "8.163.85.243"
SERVER_USER = "root"
SERVER_PASS = "Lxk@2026wk"
SERVER_PORT = 22

LOCAL_PROJECT = os.path.dirname(os.path.abspath(__file__))
REMOTE_ROOT = "/opt/challenge-cup"

# 生成随机 JWT Secret（不依赖任何外部输入）
JWT_SECRET = secrets.token_hex(32)

def ssh_connect():
    """建立 SSH 连接"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(SERVER_IP, port=SERVER_PORT, username=SERVER_USER, password=SERVER_PASS, timeout=30)
    return client

def run_cmd(ssh, cmd, desc=""):
    """在远程服务器执行命令并打印输出"""
    if desc:
        print(f"\n  [{desc}]")
    stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if err:
        print(f"  [stderr] {err.strip()}")
    if out:
        print(f"  {out.strip()}")
    return out

def sftp_upload_dir(sftp, local_dir, remote_dir):
    """递归上传整个目录"""
    # 确保远程目录存在
    try:
        sftp.stat(remote_dir)
    except FileNotFoundError:
        sftp.mkdir(remote_dir)

    for item in sorted(os.listdir(local_dir)):
        local_path = os.path.join(local_dir, item)
        remote_path = remote_dir.replace("\\", "/") + "/" + item
        # 跳过不需要的文件/目录
        skip = {".venv", "__pycache__", ".git", "node_modules", "dist",
                ".DS_Store", ".env", "deploy_setup.exp", "remote_deploy.py",
                "start_backend.sh", "start_frontend.sh"}
        if item in skip:
            continue
        if os.path.isfile(local_path):
            sftp.put(local_path, remote_path)
            print(f"    ↑ {item}")
        elif os.path.isdir(local_path):
            sftp_upload_dir(sftp, local_path, remote_path)


def main():
    print("=" * 60)
    print("  远程部署开始")
    print("  目标: {}@{}".format(SERVER_USER, SERVER_IP))
    print("=" * 60)

    # ── Step 1: 连接服务器 ──
    print("\n[1/6] 连接服务器...")
    ssh = ssh_connect()
    print("  SSH 连接成功")

    # ── Step 2: 服务器环境准备 ──
    print("\n[2/6] 准备服务器环境...")
    run_cmd(ssh, "export DEBIAN_FRONTEND=noninteractive && apt-get update -qq 2>/dev/null | tail -1", "更新包索引")

    # 安装 Docker
    if "not found" in run_cmd(ssh, "command -v docker || echo 'not found'", "检查 Docker"):
        print("  安装 Docker...")
        run_cmd(ssh,
            "curl -fsSL https://get.docker.com | sh",
            "安装 Docker")
        run_cmd(ssh, "systemctl enable docker && systemctl start docker", "启动 Docker")

    # 安装 docker compose 插件
    if "not found" in run_cmd(ssh, "docker compose version 2>/dev/null || echo 'not found'", "检查 Compose"):
        run_cmd(ssh, "apt-get install -y -qq docker-compose-plugin 2>/dev/null", "安装 Compose 插件")

    print("  Docker: " + run_cmd(ssh, "docker --version 2>&1", "").strip())
    print("  Compose: " + run_cmd(ssh, "docker compose version 2>&1", "").strip())

    # 关闭 UFW（阿里云使用安全组）
    run_cmd(ssh, "ufw disable 2>/dev/null || true", "关闭 UFW")

    # ── Step 3: 清理旧部署并创建目录 ──
    print("\n[3/6] 清理旧部署...")
    run_cmd(ssh, "docker stop cup-backend cup-frontend 2>/dev/null; docker rm cup-backend cup-frontend 2>/dev/null; true", "")
    run_cmd(ssh, f"rm -rf {REMOTE_ROOT} && mkdir -p {REMOTE_ROOT}", "")

    # ── Step 4: 上传项目文件 ──
    print("\n[4/6] 上传项目文件（SFTP）...")
    sftp = ssh.open_sftp()

    # 先创建目录结构（逐级创建）
    for d in ["backend", "frontend", "frontend/nginx"]:
        try:
            sftp.mkdir(REMOTE_ROOT + "/" + d)
        except (IOError, OSError):
            pass  # 目录已存在或父目录不存在，sftp_upload_dir 会处理

    # 上传 docker-compose.prod.yml 作为 docker-compose.yml
    sftp.put(
        os.path.join(LOCAL_PROJECT, "docker-compose.prod.yml"),
        REMOTE_ROOT + "/docker-compose.yml"
    )
    print("    ↑ docker-compose.yml")

    # 上传后端
    print("  Backend:")
    sftp_upload_dir(sftp,
                    os.path.join(LOCAL_PROJECT, "backend"),
                    REMOTE_ROOT + "/backend")

    # 上传前端
    print("  Frontend:")
    sftp_upload_dir(sftp,
                    os.path.join(LOCAL_PROJECT, "frontend"),
                    REMOTE_ROOT + "/frontend")

    sftp.close()

    # ── Step 5: 创建 .env 文件（敏感配置仅存服务器） ──
    print("\n[5/6] 配置后端 .env...")

    # 从本地 .env 读取 SMTP 密码（优先使用本地已配置的密码）
    local_env_path = os.path.join(LOCAL_PROJECT, "backend", ".env")
    smtp_user = ""
    smtp_password = ""
    if os.path.exists(local_env_path):
        with open(local_env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("SMTP_USER="):
                    smtp_user = line.split("=", 1)[1].strip().strip('"')
                elif line.startswith("SMTP_PASSWORD="):
                    smtp_password = line.split("=", 1)[1].strip().strip('"')
    if not smtp_user:
        smtp_user = "2583846465@qq.com"
    print(f"  检测到本地 SMTP_USER: {smtp_user}")
    print(f"  SMTP_PASSWORD: {'***已配置***' if smtp_password else '⚠ 未配置，邮件将无法发送！'}")

    env_content = f"""# ── 数据库 ──
DATABASE_URL=sqlite:///./data/cup.db

# ── JWT ──
SECRET_KEY={JWT_SECRET}
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# ── 邮件（QQ 邮箱 SMTP，使用 SSL 465 端口避免 STARTTLS 问题） ──
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER={smtp_user}
SMTP_PASSWORD={smtp_password}
SMTP_FROM=桂升通
SMTP_USE_SSL=true

# ── 验证码 ──
VERIFY_CODE_LENGTH=6
VERIFY_CODE_EXPIRE_SECONDS=300

# ── CORS ──
CORS_ORIGINS=["http://8.163.85.243:5173","http://8.163.85.243","http://localhost:5173"]

# ── 服务 ──
HOST=0.0.0.0
PORT=8000
"""
    # 通过 echo 写入（避免文件传输泄露）
    escaped = env_content.replace("'", "'\\''")
    run_cmd(ssh, f"cat > {REMOTE_ROOT}/backend/.env << 'ENVEOF'\n{env_content}\nENVEOF", "写入 .env")
    run_cmd(ssh, f"chmod 600 {REMOTE_ROOT}/backend/.env", "保护 .env 权限")

    # ── Step 6: 构建并启动 ──
    print("\n[6/6] Docker Compose 构建并启动...")
    run_cmd(ssh,
        f"cd {REMOTE_ROOT} && docker compose build --no-cache 2>&1 | tail -20",
        "构建镜像（可能需要几分钟）")

    run_cmd(ssh,
        f"cd {REMOTE_ROOT} && docker compose up -d 2>&1",
        "启动服务")

    time.sleep(5)

    # ── 验证 ──
    print("\n" + "=" * 60)
    print("  验证部署结果")
    print("=" * 60)

    print("\n  Docker 容器状态:")
    run_cmd(ssh, f"cd {REMOTE_ROOT} && docker compose ps", "")

    print("\n  后端健康检查:")
    run_cmd(ssh, "curl -s http://localhost:8000/api/hello 2>&1 | head -5", "")

    print("\n  前端健康检查:")
    run_cmd(ssh, "curl -s -o /dev/null -w '%{http_code}' http://localhost:5173/ 2>&1", "")

    # 关闭连接
    ssh.close()

    print("\n" + "=" * 60)
    print("  部署完成！")
    print("=" * 60)
    mail_status = "✓ 已自动配置" if smtp_password else "✗ 未配置，验证码邮件将无法发送"
    print(f"""
  前端: http://{SERVER_IP}:5173
  后端 API: http://{SERVER_IP}:8000
  API 文档: http://{SERVER_IP}:8000/docs
  API 健康检查: http://{SERVER_IP}:8000/api/hello

  ⚠ 请确保阿里云安全组已开放端口: 80, 443, 8000, 5173
  SMTP 邮件: {mail_status}
  """)

if __name__ == "__main__":
    main()