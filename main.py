from settings import OPERATION_DATA_PATH, OPERATION_COUNT
from src.utils import load_json_data, get_executed_operations, get_operation_instances, sort_operations_by_date

operations_data = load_json_data(OPERATION_DATA_PATH)
executed_operations = get_executed_operations(operations_data)
operation_instances = get_operation_instances(executed_operations)
sort_operations = sort_operations_by_date(operation_instances)

for operation in sort_operations[:OPERATION_COUNT]:
    print(operation)
