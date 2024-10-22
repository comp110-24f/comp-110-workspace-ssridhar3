"""ex05: utils_test Due: Tuesday, October 22"""

__author__: str = "730771829"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


# Test cases for only_events
def test_only_evens_all_even_numbers():
    """Tests only_evens when it has a list of all even numbers."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_mixed_numbers():
    """Tests only_evens wwhen there are both odd and even numbers."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_empty_list():
    """Tests only_evens when there is nothing in a list"""
    assert only_evens([]) == []


# Test cases for sub
def test_sub_normal_ranged():
    """Tests sub with a normal range of indexes"""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_negative_index():
    """Tests sub with a start index that is negative"""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -1, 2) == [10, 20]


def test_sub_greater_end():
    """Tests sub with an end index that is greater than the length of the list"""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 10) == [20, 30, 40]


# Test cases for add_at_index
def test_add_at_middle():
    """Tests adding an element in the middle of the list"""
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]


def test_add_at_start():
    """Tests adding an element at the start of the list"""
    list_2 = [2, 3, 4]
    add_at_index(list_2, 1, 0)
    assert list_2 == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Tests that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list_3 = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list_3, 4, -1)  # Invalid negative index
    with pytest.raises(IndexError):
        add_at_index(list_3, 4, 10)  # Invalid index greater than length.
