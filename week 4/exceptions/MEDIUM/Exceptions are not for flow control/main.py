class AdminFound(Exception):
    def __init__(self, admin_user):
        self.user = admin_user

def find_first_admin_bad(users):
    for user in users:
        if user.get("role") == "admin":
            raise AdminFound(user)
    return None # Если не нашли

# ---
users_list = [{"name": "Bob", "role": "user"}, {"name": "Alice", "role": "admin"}]

try:
    find_first_admin_bad(users_list)
except AdminFound as e:
    print(f"Администратор найден (плохой способ): {e.user['name']}")


def find_first_admin_good(users: list) -> dict | None:
    """
    Находит первого пользователя с ролью 'admin'.
    
    Использует 'return' для немедленного выхода и возврата 
    найденного пользователя.
    """
    for user in users:
        # 2. Используем if для проверки
        if user.get("role") == "admin":
            # 3. Используем return, как только нашли
            return user
    
    # 4. Возвращаем None, если цикл завершился, а админ не найден
    return None

# --- Пример использования ---
users_list = [
    {"name": "Bob", "role": "user"}, 
    {"name": "Alice", "role": "admin"},
    {"name": "Charlie", "role": "admin"} # До этого не дойдет
]

print("--- Поиск хорошим способом ---")

# 5. Вызываем функцию и проверяем результат через if
admin = find_first_admin_good(users_list)

if admin:
    print(f"Администратор найден: {admin['name']}")
else:
    print("Администратор не найден.")

# Пример с пустым списком или без админа
users_list_no_admin = [
    {"name": "Bob", "role": "user"}, 
    {"name": "Eve", "role": "guest"}
]

print("\n--- Поиск в списке без админов ---")
admin_none = find_first_admin_good(users_list_no_admin)

if admin_none:
    print(f"Администратор найден: {admin_none['name']}")
else:
    print("Администратор не найден.")