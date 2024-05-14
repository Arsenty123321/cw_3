import pytest

from src.classes import Operation
from src.utils import get_executed_operations, sort_operations_by_date


def test_get_executed_operations():
    operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
        {
            "state": "NO_VALID_STATE",
        },
        {},
    ]
    expected_operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
    ]
    assert get_executed_operations(operations) == expected_operations
    assert get_executed_operations([]) == []


@pytest.fixture
def operation_fixture():
    operation_instances = []
    op1 = Operation(
        pk=111111111,
        state="EXECUTED",
        date="2018-12-29T21:45:18.495056",
        amount="66263.93",
        currency="руб.",
        description="Перевод организации",
        to_="Счет 48943806953649539453",
        from_="Visa Gold 7756673469642839",
    )
    op2 = Operation(
        pk=222222222,
        state="EXECUTED",
        date="2019-11-20T22:46:19.495053",
        amount="66263.93",
        currency="руб.",
        description="Перевод организации",
        to_="Счет 48943806953649539453",
        from_=None
    )
    operation_instances.append(op1)
    operation_instances.append(op2)
    return operation_instances


def test_operation_instance_init(operation_fixture):
    operation = operation_fixture[0]
    assert operation.from_ == "Visa Gold 7756 67** **** 2839"
    assert operation.to_ == "Счет **9453"


def test_operation_instance_convert_payment_date(operation_fixture):
    operation = operation_fixture[0]
    assert operation.convert_payment_date() == "29.12.2018"


def test_operation_instance_hide_payment_data(operation_fixture):
    operation = operation_fixture[0]
    assert operation.hide_payment_data("МИР 1582474475547301") == "МИР 1582 47** **** 7301"


def test_operation_instance_str_(operation_fixture):
    operation = operation_fixture[0]
    assert str(operation) == (
        "29.12.2018 Перевод организации\n"
        "Visa Gold 7756 67** **** 2839 -> Счет **9453\n"
        "66263.93 руб.\n"
    )


def test_sort_operations_by_date(operation_fixture):
    operations = operation_fixture
    sort_operations = sort_operations_by_date(operations)
    assert sort_operations[0].date == "2019-11-20T22:46:19.495053"


def test__operation_instance_with_none_from_(operation_fixture):
    operation = operation_fixture[1]
    assert operation.from_ == ""
