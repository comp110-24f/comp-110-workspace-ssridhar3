"""EX04 - list Utility Functions Due: Sunday, October 13"""

__author__: str = "730771829"


def all(int_list: list[int], target: int) -> bool:
    """This returns True if all the items in the list match the target integer"""
    if len(int_list) == 0:  # this says if the list is empty, return False
        return False
    for num in int_list:  # this will loops through each item in the list
        if num != target:
            return False  # False will be returned if any item does not match
    return True  # True will be returned if all items match the target


def max(input: list[int]) -> int:
    """Returns the largest number. If the list is empty, will raise ValueError"""
    if len(input) == 0:  # checks if list is empty
        raise ValueError("max() arg is an empty list")
    max_value = input[0]
    for num in input:
        if num > max_value:
            max_value = num
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This will return True if both lists have the same length and items"""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates list1 by appending all elements of list2 to the end of it"""
    for element in list2:
        list1.append(element)


# Testing the functions

# all function
print(all([1, 2, 3], 1))  # Output: False
print(all([1, 1, 1], 1))  # Output: True
print(all([], 1))  # Output: False

# max function
print(max([1, 3, 2]))  # Output: 3
print(max([100, 99, 98]))  # Output: 100

# is_equal function
print(is_equal([1, 0, 1], [1, 0, 1]))  # Output: True
print(is_equal([1, 1, 0], [1, 0, 1]))  # Output: False

# extend function
a = [1, 3, 5]
b = [2, 4, 6]
extend(a, b)
print(a)  # Output: [1, 3, 5, 2, 4, 6]
