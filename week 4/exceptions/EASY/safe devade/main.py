def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
        return None
    else:
        return result
    
print(safe_divide(10, 2))  # Ожидаемый вывод: 5.0
print(safe_divide(10, 0))  # Ожидаемый вывод: Ошибка: Деление на ноль невозможно. None