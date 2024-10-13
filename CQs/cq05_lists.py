"""Mutating Functions."""

__author__: str = "730771829"

from typing import List


def manual_append(lst: List[int], value: int) -> None:
    """This function will append an integer to the end of a list of integers"""
    """list (List[int]): is the list to be mutated"""
    """ value(int) is the integer that will be appened."""

    lst.append(value)


def double(lst: List[int]) -> None:
    index: int = 0
    while index < len(lst):
        lst[index] *= 2
        index += 1


"""I made mine more concise using the lst[index] *= 2"""

list_1: List[int] = [1, 2, 3]
list_2: List[int] = list_1

double(list_2)

print("list_1:", list_1)
print("list_2:", list_2)
