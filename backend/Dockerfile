FROM python:3.12-slim

# 避免 .pyc 文件和输出缓冲
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 安装系统依赖（psycopg2 编译需要 libpq-dev，生产用 gcc 编译后清理）
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖（使用清华镜像加速）
COPY requirements.txt .
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 复制项目
COPY . .

# 清理编译工具（减小镜像体积）
RUN apt-get purge -y gcc && apt-get autoremove -y

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]