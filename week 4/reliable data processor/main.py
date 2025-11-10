from my_utils import (
    setup_logging, 
    UserData,
    timer,
    DataProcessorError, 
    DataSourceError, 
    DataParsingError
)
import logging
from pathlib import Path
from my_utils import setup_logging, DataProcessorError
from processing import process_user_data

def create_test_file(file_path: Path):
    """Create a test CSV file with "good" and "bad" data."""
    logger = logging.getLogger(__name__)
    logger.info(f"test file create: {file_path.name}")

    csv_content = (
        "id,name,email\n" # header
        "1,Ivan Petrov,ivan@example.com\n" # ok
        "2,Anna Smirnova,anna@example.com\n" # ok
        "bad_id,Oleg,oleg@example.com\n" # error ValueError
        "4,Maria,maria@exapmle.com,extra field\n" # error DataParsingError
        "5,Petr\n" # error IndexError -> DataParsingError
        "6,Elena,elena@exapmle.com\n" # ok
        ",empty ID,empty@example.com\n" # error ValueError
        "8,Stepan,\n" # error DataParsingError (empty email)
        "9,Alice,alice@example.com\n" # ok
    )

    try:
        file_path.write_text(csv_content, encoding="utf-8")
    except IOError as e:
        logger.error(f"failed to create test file: {e}")
        raise # raise as error if we can't create the file

def main() -> None:
    """
    main "entry point" to the application
    """
    # setting up logging (the first and most important step)
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("="*30 + " START APPLOCATION " + "="*30)

    INPUT_FILE = Path("users.csv")
    OUTPUT_FILE = Path("users_report.json")

    try:
        create_test_file(INPUT_FILE)
        logger.info(f"starting main processing: {INPUT_FILE.name}")
        count = process_user_data(INPUT_FILE, OUTPUT_FILE)

        logger.info(f"--- ОБРАБОТКА УСПЕШНА ---")
        logger.info(f"Успешно обработано: {count} записей.")
        logger.info(f"Отчет сохранен в: {OUTPUT_FILE.resolve()}")
        print(f"\nУспешно обработано: {count} записей.")
        print(f"Отчет сохранен в: {OUTPUT_FILE.name}")
    except DataProcessorError as e:
        # 5. Ловим наши *ожидаемые* ошибки (DataSourceError, DataParsingError)
        logger.critical(f"Критическая ошибка обработки данных: {e}")
        print(f"\nКРИТИЧЕСКАЯ ОШИБКА: {e}. Выполнение прервано.")
        print("Подробности см. в файле processing.log")

    except Exception as e:
        # 6. Ловим *неожиданные* ошибки (баги в коде)
        logger.exception(f"Неожиданная фатальная ошибка: {e}", exc_info=True)
        print(f"\nНЕОЖИДАННАЯ ОШИБКА: {e}. Выполнение прервано.")
        print("Подробности см. в файле processing.log")

    logger.info("="*30 + " ЗАВЕРШЕНИЕ ПРИЛОЖЕНИЯ " + "="*30)

if __name__ == "__main__":
    main()






#if __name__ == "__main__":
#    logger.info("="*30 + " Start project " + "="*30)
#
#    input_file = Path("users.csv")
#    output_file = Path("user_report.json")
#
#    try:
#        # --- preparation ---
#        create_test_csv(input_file)
#
#        # --- execution ---
#        count = process_user_data(input_file, output_file)
#
#        logger.info(f"--- RESULT: processing completed successfully ---")
#        logger.info(f"successful entries: {count}")
#        logger.info(f"the report is saved in {output_file.resolve()}")
#
#    except DataProcessorError as e:
#        # we catch "any" error we make (DataSourceError, DataParsingError)
#        logger.critical(
#            f"--- CRITICAL ERROR: processing interrupted"
#            f"{e.__class__.__name__}: {e} ---"
#        )
#    except Exception as e:
#        logger.critical(
#            f"--- UNEXPECTED ERROR: {e} ---", exc_info=True
#        )
#
#    logger.info("="*30 + "completion of the project" + "="*30)
#




# Пишем основную логику, используя импортированные классы
#def process_data_file(file_path):
#    logger.info("starting user create")
#    user_alice: UserData = {
#        "id": 1,
#        "name": "Alice",
#        "email": "alice@example.com"
#    }
#    logger.info(f"Успешно создан пользователь: {user_alice}")
#
#    try:
#        logger.info(f"start processing the file: {file_path}")
#        raise DataSourceError(f"file '{file_path}' not found")
#    except DataProcessorError as e:
#        # Ловим ОБЩУЮ ошибку
#        logger.error(f"Ошибка при обработке данных: {e.__class__.__name__} - {e}")
#    except Exception as e:
#        # Ловим любые другие (непредвиденные) ошибки
#        logger.critical(f"Неожиданная ошибка: {e}", exc_info=True)
#
#def run_successful_task():
#    try:
#        with timer(logger, "Успешная обработка данных"):
#            logger.info("...выполняется какая-то работа...")
#            time.sleep(0.1) # Имитация работы
#            logger.info("...работа почти завершена...")
#            time.sleep(0.2) # Имитация работы
#        print("[main.py] Блок 'with' успешно завершен.\n")
#    except Exception:
#        # Сюда мы попасть не должны
#        print("[main.py] Была поймана ошибка (неожиданно).\n")
#
#def run_failed_task():
#    """Имитация задачи, которая "падает" с ошибкой."""
#    try:
#        # Используем timer для задачи, которая "упадет"
#        with timer(logger, "Рискованная операция (деление на ноль)"):
#            logger.info("...начинаем рискованную операцию...")
#            time.sleep(0.1)
#            
#            # Имитируем ошибку (эта ошибка будет поймана *внутри* timer)
#            result = 10 / 0 
#        
#        print("[main.py] Блок 'with' завершен (ЭТО НЕ ДОЛЖНО ПОЯВИТЬСЯ).\n")
#
#    except ZeroDivisionError as e:
#        # Мы попадаем сюда, потому что timer "пробросил" ошибку наружу
#        logger.warning(f"[main.py] Успешно поймали ошибку: {e}\n")
#    except DataProcessorError as e:
#        # Также могли бы ловить наши кастомные ошибки
#        logger.error(f"[main.py] Поймана наша кастомная ошибка: {e}\n")
#
#if __name__ == "__main__":
#    logger.debug("Старт программы")
#    process_data_file("non_existent_file.json")
#    run_successful_task()
#    run_failed_task()
#    logger.debug("Завершение программы")