import json
from pathlib import Path

from typing import List


def load_json_data(path: Path) -> List[dict]:
    """
    :param path: Путь к файлу с данными
    :return: Возвращает словарь с данными
    """

    with open(path, encoding='UTF-8') as file:
        return json.load(file)


def get_executed_operations(operations: List[dict]):
    """
    :param operations: Словарь с данными операций
    :return: Возвращает словарь с executed операциями
    """
    return [operation for operation in operations if operation.get("state") == "EXECUTED"]
