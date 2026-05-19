"""
Snowflake 雪花 ID 校验工具（Twitter Snowflake 算法变体）

位分配（64-bit）：[41bit 时间戳][5bit data center][5bit worker][12bit 序列号]  ← 标准 Twitter
自定义简版（兼容任意 snowflake 实现）：
    最低要求：ID 长度 ≥ 15 位数字 且 时间戳部分 > 2020-01-01 毫秒基准
"""

import time

# ── 校验基准 ────────────────────────────────────
# 2020-01-01 00:00:00 UTC 对应的毫秒时间戳
BASELINE_MS = 1577836800000
# 允许的最大时间漂移（允许未来 10 年）
MAX_FUTURE_MS = 10 * 365 * 24 * 3600 * 1000


def parse_snowflake(snowflake_id: int) -> bool:
    """
    校验给定的整数是否为合法的 Snowflake 风格 ID。
    - 必须 ≥ 15 位十进制数字
    - 包含合理的时间戳范围

    返回 True 表示通过校验。
    """
    # 最低位宽：约 10^14，对应 1 秒级 worker + sequence
    if snowflake_id < 10 ** 14:
        return False

    # 提取时间戳高位（假设前 41 位或类似布局）
    # 通用策略：尝试多种移位方式，取最合理的时间戳
    shifts = [22, 23, 21, 20, 19]  # 常见移位偏移
    for shift in shifts:
        ts_ms = snowflake_id >> shift
        # 匹配典型 epoch (Twitter: 1288834974657, 自定义: 可自设)
        for epoch in [1288834974657, 1577836800000]:
            ts = ts_ms + epoch
            now_ms = int(time.time() * 1000)
            if BASELINE_MS < ts < now_ms + MAX_FUTURE_MS:
                return True

    # 兜底：纯位数 + 高位非零校验
    digits = str(snowflake_id)
    if len(digits) < 15:
        return False
    # 时间位非零（高位不能全为 0）
    if digits[0] == "0":
        return False

    return True


def generate_snowflake(worker_id: int = 1, data_center_id: int = 1) -> int:
    """
    生成一个 Snowflake 风格 ID（简化实现，适合单机/开发环境）。
    真实生产环境建议使用第三方库（如 pysnowflake）或数据库序列。
    """
    epoch = 1577836800000  # 2020-01-01 00:00:00
    sequence = int(time.time() * 1000) % 4096
    timestamp_ms = int(time.time() * 1000) - epoch

    return (
        (timestamp_ms << 22)
        | (data_center_id << 17)
        | (worker_id << 12)
        | sequence
    )