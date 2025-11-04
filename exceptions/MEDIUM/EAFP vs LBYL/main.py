# LBYL ("Смотри, прежде чем прыгнуть")

def get_name_lbyl(user: dict) -> str:
    """
    Получает имя в стиле LBYL.
    Сначала проверяет, потом действует.
    """
    if "name" in user:
        return user["name"]
    else:
        return "Гость"
    
# EAFP ("Проще попросить прощения")

def get_name_eafp(user: dict) -> str:
    """
    Получает имя в стиле EAFP (предпочитаемый в Python).
    Сначала действует, потом ловит ошибку.
    """
    try:
        return user["name"]
    except KeyError:
        return "Гость"