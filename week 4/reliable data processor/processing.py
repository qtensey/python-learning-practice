import csv
import json
import logging
from pathlib import Path
from typing import List

from my_utils import (
    timer,
    UserData,
    DataSourceError,
    DataParsingError
)

logger = logging.getLogger(__name__)

def process_user_data(input_path: Path, output_path: Path) -> int:
    """
    reads csv-file, validates data, writes "clean" data to a JSON report.

    returns:
        int: number of successfuly process records.

    raise:
        DataSourceError: if tje file not found or could not be read/written.
        DataParsingError: (intercepted internally) for "broken" lines.
    """
    logger.info(f"Start processing: {input_path.name} -> {output_path.name}")

    with timer(logger, f"full file processing {input_path.name}"):
        
        clean_data: List[UserData] = []

        # -----------------------------------------------------------------
        # BLOCK 1: reading a file (with FileNotFoundError handling)    
        # -----------------------------------------------------------------
        try:
            with input_path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f) # создает "конвейер"

                try:
                    header = next(reader) # "снимает" с этого конвейера первый элемент.
                    logger.debug(f"Title read: {header}.")
                except StopIteration:
                    logger.warning(f"file {input_path.name} empty.")
                    return 0 # 0 успешных записей

                # ---------------------------------------------------------
                # BLOCK 2: data processing (line by line with EAFP)
                # ---------------------------------------------------------
                # i - line number for logs
                for i, row in enumerate(reader, start=2):
                    try:
                        # 1. Валидация (это не EAFP, но это хорошая практика)
                        if len(row) != 3:
                            raise DataParsingError(
                                f"Ожидалось 3 столбца, получено {len(row)}"
                            )
                        
                        # 2. Попытка приведения типов (здесь EAFP ловит ValueError)
                        user_id = int(row[0])
                        user_name = row[1]
                        user_email = row[2]

                        if not user_name or not user_email:
                            raise DataParsingError("name or email cannot by empty")
                        
                        user: UserData = {
                            "id": user_id,
                            "name": user_name,
                            "email": user_email
                        }

                        clean_data.append(user)

                    # 4. Обработка "плохих" строк (EAFP)
                    except (ValueError, DataParsingError, IndexError) as e:
                        logger.warning(
                            f"skip line {i} (data: {row}): {e}"
                        )
                        continue # Переходим к следующей строке

        except FileNotFoundError as e:
            logger.error(f"data source not found: {input_path}")
            # Оборачиваем ошибку в наше кастомное исключение (как в задании)
            raise DataSourceError(f"file not found: {input_path}") from e
        except Exception as e:
            # Ловим другие ошибки чтения (например, права доступа)
            logger.error(f"an unexpected error occurred while reading file: {e}")
            raise DataSourceError(f"reading file error: {e}") from e
        
        # -----------------------------------------------------------------
        # BLOCK 3: write report (JSON)
        # -----------------------------------------------------------------

        logger.info(
            f"processing complete. successfull entries: {len(clean_data)}"
        )
        if not clean_data:
            logger.info("there is not data to record in the report")
            return 0
        
        try:
            json_data = json.dumps(
                clean_data,
                indent=2,
                ensure_ascii=False # for correct display Cyrillic
            )

            # atomaric writen (write_text)
            output_path.write_text(json_data, encoding="utf-8")
        except (IOError, PermissionError) as e:
            logger.error(f"filed to write report file: {output_path}")
            raise DataSourceError(
                f"write error, check permisions: {output_path}"
            ) from e
        
        return len(clean_data)