import logging
import logging.config
import sys
import time
from typing import TypedDict
from contextlib import contextmanager

# ---------------------------------------------------------------------------
# exercise 1.3: Определение своих исключений
# ---------------------------------------------------------------------------
# Определяем их вначале, чтобы они были доступны во всем модуле.

class DataProcessorError(Exception):
    """Базовое исключение для ошибок при обработке данных."""
    pass

class DataSourceError(DataProcessorError):
    """Исключение, возникающее при ошибках чтения/доступа к источнику данных."""
    pass

class DataParsingError(DataProcessorError):
    """Исключение, возникающее при ошибках парсинга или валидации данных."""
    pass

# -----------------------------------------------------------------
# exercise 1.2: Определение типов данных
# -----------------------------------------------------------------

class UserData(TypedDict):
    """
    Типизированный словарь ("чертеж") для данных пользователя.
    """
    id: int
    name: str
    email: str

# -----------------------------------------------------------------
# Задание 1.1: Настройка логирования
# -----------------------------------------------------------------

def setup_logging():
    """
    Настраивает конфигурацию логирования для проекта.
    - В файл 'processing.log' пишутся логи с уровня DEBUG.
    - В консоль (stdout) пишутся логи с уровня INFO.
    """
    # Определяем конфигурацию для dictConfig
    LOGGING_CONFIG = {
        'version': 1, # Обязательный ключ
        'disable_existing_loggers': False, # Не отключать существующие логгеры

        # Форматтеры (определяют, как будет выглядеть сообщение)
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },

        # Обработчики (handlers), - куда писать логи
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': sys.stdout, # Явно указываем поток вывода (консоль)
            },
            'file': {
                'level': "DEBUG",
                'class': 'logging.FileHandler',
                'filename': 'processing.log',
                'mode': 'w', # 'w' - перезаписывать файл при каждом запуске
                'formatter': 'standard',
                'encoding': 'utf-8',
            },
        },

        # Логгеры
        'loggers': {
            # Корневой логгер (пустая строка)
            '': {
                'handlers': ['console', 'file'], # Применяем оба обработчика
                'level': 'DEBUG', # Минимальный уровень, который "ловит" логгер
                                # (DEBUG, т.к. файлу нужен DEBUG)
                'propagate': True,
            },
        }
    }

    try:
        logging.config.dictConfig(LOGGING_CONFIG)
        logging.info("Система логирования успешно настроена.")
    except Exception as e:
        print(f"Ошибка при настройке логирования: {e}")
        logging.basicConfig(level=logging.INFO) # Запасной вариант
        logging.error("Не удалось настроить dictConfig, используется basicConfig.")

# -----------------------------------------------------------------
# Задание 2: Менеджер контекста
# -----------------------------------------------------------------

@contextmanager
def timer(logger: logging.Logger, task_name: str):
    """
    Менеджер контекста для замера времени выполнения 
    и логирования ошибок.
    """
    logger.info(f"Начало задачи: {task_name}...")
    start_time = time.perf_counter()

    try:
        # "Пропускаем" управление внутрь блока 'with'
        yield
    except Exception as e:
        logger.exception(f"Ошибка в задаче '{task_name}': {e}")
        raise # Пробрасываем ошибку дальше
    finally:
        end_time = time.perf_counter()
        duration = end_time - start_time
        logger.info(f"Задача '{task_name}' завершена за {duration:.4f} сек.")