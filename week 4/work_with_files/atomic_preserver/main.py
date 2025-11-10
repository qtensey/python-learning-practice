import os, tempfile
from pathlib import Path

def atomic_write_text(path: Path, text: str, encoding="utf-8") -> None:
    tmp_fd, tmp_name = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(tmp_fd, "w", encoding=encoding, newline="") as tmp:
            tmp.write(text)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_name, path)   # атомарно подменяет
    finally:
        try: os.remove(tmp_name)
        except FileNotFoundError: pass