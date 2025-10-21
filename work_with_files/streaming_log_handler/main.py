from pathlib import Path
import json

def count_logins(log_path: Path) -> int:
    login_count = 0
    try:
        with log_path.open(mode='r', encoding='utf-8') as f:
            for line in f:
                try:
                    event = json.loads(line)
                    if event.get("event") == "login":
                        login_count += 1
                except json.JSONDecodeError:
                    print(f"Пропущена некорректная строка: {line.strip()}")
    except FileNotFoundError:
        print("Файл логов не найден.")
        
    print(f"Количество логинов: {login_count}")
    return login_count

BASE_DIR = Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "events.ndjson"

count_logins(LOG_PATH)