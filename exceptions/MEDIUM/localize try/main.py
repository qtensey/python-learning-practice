def find_user_by_id(user_id):
    if user_id == 10:
        print({"name": "Alice"})
        return {"name": "Alice"}
    # Имитируем, что другие ID не найдены
    raise KeyError(f"Пользователь {user_id} не найден")

def process_user_input():
    try:
        user_input = input("Введите ID пользователя: ")
        user_id = int(user_input)
    except ValueError:
        print("incorrect id value entered.")
        return

    try:
        user = find_user_by_id(user_id)
    except KeyError:
        print(f"Пользователь {user_id} не найден")

process_user_input()