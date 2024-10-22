"""ex05: utils Due: Tuesday, October 22"""

__author__: str = "730771829"


def only_evens(input_list: list[int]) -> list[int]:
    """Will return a new list containing only the even integers from input list"""
    result = []
    for number in input_list:
        if number % 2 == 0:
            result.append(number)
    return result


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Will return a subset of he input list"""
    result = []
    length = len(input_list)

    if start_index < 0:
        start_index = 0
    if end_index > length:
        end_index = length

    if length == 0 or start_index >= length or end_index <= 0:
        return result

    for i in range(start_index, end_index):
        result.append(input_list[i])
    return result


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    """Adds an element at a specific index in the input list"""
    if index < 0 or index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")

    input_list.append(0)

    for i in range(len(input_list) - 1, index, -1):
        input_list[i] = input_list[i - 1]

    input_list[index] = element
