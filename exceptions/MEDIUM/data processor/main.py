import logging

def process_data_list(data_list):
    total_sum = 0

    for item in data_list:
        try:
            total_sum += item["value"]
        except KeyError:
            logging.exception(f"Не удалось обработать элемент: {item}")
            # 7. Продолжаем цикл, переходя к следующему элементу
            continue
    return total_sum

data = [
    {"id": 1, "value": 10},
    {"id": 2}, # <-- Отсутствует ключ 'value'
    {"id": 3, "value": 30},
]

print("--- Начало обработки ---")
total = process_data_list(data)
print("--- Конец обработки ---")

print(f"\nИтоговая сумма: {total}")