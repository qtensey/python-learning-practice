from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
#PROJECT_DIR = BASE_DIR.parent
CORRECT_PATH = BASE_DIR / "data" / "correct.json"
BROKEN_PATH = BASE_DIR / "data" / "broken.json"
INVALID_PATH = BASE_DIR / "data" / "invalid.json"

def load_config(config_path: Path) -> dict:
    try:
        text = config_path.read_text(encoding='utf-8')
        data = json.loads(text)
        print(text)
        print(data)
    except FileNotFoundError:
        print("Конфиг не найден, используются значения по умолчанию")
        return {}
    except json.JSONDecodeError as e:
        print("Ошибка: конфиг поврежден (невалидный JSON)!")
        return {}


load_config(CORRECT_PATH)
load_config(BROKEN_PATH)
load_config(INVALID_PATH)