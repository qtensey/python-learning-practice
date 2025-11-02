def get_setting(config_dict, key):
    try:
        return config_dict[key]
    except KeyError:
        return None
    
config = {
    "username": "admin",
    "theme": "dark",
    "timeout": 30
}

# 1. Пытаемся получить существующий ключ
theme_setting = get_setting(config, "theme")
print(f"Значение для 'theme': {theme_setting}")

# 2. Пытаемся получить НЕсуществующий ключ
font_setting = get_setting(config, "font_size")
print(f"Значение для 'font_size': {font_setting}")

# 3. Еще один существующий ключ
user_setting = get_setting(config, "username")
print(f"Значение для 'username': {user_setting}")