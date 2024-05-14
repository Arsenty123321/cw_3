import json
from pathlib import Path
from typing import List
from src.classes import Operation


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
    :return: Возвращает словарь только с executed операциями
    """
    return [operation for operation in operations if operation.get("state") == "EXECUTED"]


def get_operation_instances(operations: List[dict]) -> List[Operation]:
    """
    :param operations: Получает словарь с операциями
    :return: Возвращает список экземпляров класса Operation с заполненными атрибутами
    """
    operation_instances = []
    for operation in operations:
        operation_amount = operation["operationAmount"]
        op = Operation(
            date=operation["date"],
            pk=operation["id"],
            state=operation["state"],
            amount=operation_amount["amount"],
            currency=operation_amount["currency"]["name"],
            description=operation["description"],
            to_=operation["to"],
            from_=operation.get("from"),
        )
        operation_instances.append(op)
    return operation_instances


def sort_operations_by_date(operations: List[Operation]) -> List[Operation]:
    """
    :param operations: Получает список экземпляров класса
    :return: Возвращает отсортированный список экземпляров класса
    """
    return sorted(operations, reverse=True)
