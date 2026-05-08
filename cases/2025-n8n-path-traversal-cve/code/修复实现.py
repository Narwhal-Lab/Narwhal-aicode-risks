# 代表性安全修复
# 目标：1) allowlist 文件名 2) canonicalize 路径 3) 确保仍在 base 目录下

import re
import urllib.parse
from pathlib import Path

FILENAME_RE = re.compile(r"^[a-zA-Z0-9_\-]+\.json$")

def validate_filename(raw: str) -> str:
    decoded = raw
    for _ in range(3):  # 防止嵌套编码绕过
        decoded = urllib.parse.unquote(decoded)
    if not FILENAME_RE.match(decoded):
        raise ValueError("invalid filename")
    # 明确拒绝任何目录分隔与遍历语义（含 Windows/Unix）
    if any(x in decoded for x in ["..", "/", "\\", ":", "\x00"]):
        raise ValueError("path traversal detected")
    return decoded

def resolve_safe(base_dir: Path, filename: str) -> Path:
    base = base_dir.resolve()
    candidate = (base / filename).resolve()
    candidate.relative_to(base)  # 逃逸则抛异常
    return candidate
