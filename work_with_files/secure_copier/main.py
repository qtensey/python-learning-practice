from pathlib import Path

def copy_large_file(source: Path, destination: Path):
    CHUNK_SIZE = 1024 * 1024  # 1 MB
    try:
        with source.open(mode='rb') as src_file, destination.open(mode='wb') as dest_file:
            while chunk := src_file.read(CHUNK_SIZE):
                dest_file.write(chunk)
        print(f"Файл успешно скопирован из {source} в {destination}")
    except FileNotFoundError:
        print("Исходный файл не найден.")

BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "image.jpg"
DESTINATION_PATH = BASE_DIR / "copied_image.jpg"

copy_large_file(SOURCE_PATH, DESTINATION_PATH)