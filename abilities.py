from typing import Dict, Any

def key_value_storage(operation: str, group: str, key: str, value: str) -> Dict[str, Any]:
    """
    Stores and retrieves data to be persisted between application executions, for 'store' operation.
    
    Args:
        operation (str): One of the following values: 'store', 'retrieve' and 'delete'.
        group (str): The name of the application without spaces.
        key (str): a distinct, non-empty and unique identifier for each item to be stored.
        value (str): the value that needs to be stored convert non string values to string, cannot be empty for create or 'store' operation, has to be empty for other operations, the values has to be string.


    Returns:
        Dict[str, Any]: A dict which contains upstream_service_result_code, HTTP result code from the key_value storage service, values are as following 201 for success create, 200 for success retrieve, 204 for empty retrieve, 422 for invalid input, 500 for server errors (a int) and kv_pairs, A list of records as dictionary where the properties are 'key' and 'value' (a List[Dict[str, str]])

    Raises:
        Exception: This function can raise an exceptions but it is not possible to detail here which ones can be raised.

    Additional dependencies:
        No additional dependencies needed.

    Setup:
        No additional setup needed.

    Constraints or Limitations:
        Assume none.
    """