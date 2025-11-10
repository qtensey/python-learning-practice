import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "report.csv"

users = [
    {"id": 1, "name": "Алиса", "email": "alice@example.com"},
    {"id": 2, "name": "Борис", "email": "boris@example.com"},
]

def save_report(users_list: list, output_path: Path):
    fieldnames = ["id", "name", "email"]
    with output_path.open(mode='w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for user in users_list:
            writer.writerow(user)
        

save_report(users, OUTPUT_PATH)