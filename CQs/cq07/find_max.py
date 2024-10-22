"""CQ07 - find_max"""

__author__ = "730771829"


def find_and_remove_max(lst: list[int]) -> int:
    """This will check if the input list is empty"""
    if not lst:
        return -1

    """This will find the largest value in the list"""
    max_value = max(lst)

    """A while loop is used to remove all of the times the largest value occurs"""
    while max_value in lst:
        lst.remove(max_value)

    return max_value
