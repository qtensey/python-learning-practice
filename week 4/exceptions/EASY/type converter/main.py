def safe_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("Ошибка: Невозможно преобразовать это значение в число")
    except TypeError:
        print("Ошибка: Неверный тип данных")
    
print(safe_to_int("123"))    # Ожидаемый вывод: 123
print(safe_to_int("abc"))    # Ожидаемый вывод: Ошибка:
print(safe_to_int([1,2,3]))