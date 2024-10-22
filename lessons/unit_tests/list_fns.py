def get_first(input: list[str]) -> str:
    """Takes a list[str] as input and returns first element"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Takes a list[str] as input and removes first element (doesn't return anything)"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Takes a list[str] as input and returns + removes first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
