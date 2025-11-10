def validate_password(password: str):
    if len(password) < 8:
        # 1. Сами "поднимаем" исключение, если условие не выполнено
        raise ValueError("Пароль слишком короткий (менее 8 символов)")
    print("password accepted.")

try:
    validate_password("shoasdsadasrt")
except ValueError as e:
    print(f"Ошибка валидации: {e}")