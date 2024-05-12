import json
from pathlib import Path


def load_json_data(path: Path):
    """
    :param path: Путь к файлу с данными
    :return: Возвращает словарь с данными
    """

    with open(path, encoding='UTF-8') as file:
        return json.load(file)
