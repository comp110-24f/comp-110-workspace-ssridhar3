"""CQ07: max_test"""

__author__ = "730771829"

import unittest
from find_max import find_and_remove_max
from typing import List


class TestFindAndRemoveMax(unittest.TestCase):

    def test_returns_max_value(self) -> None:
        """Tests that the fuction returns the correct maximum value"""
        self.assertEqual(find_and_remove_max([3, 8, 1, 6]), 8)

    def test_list_mutation(self) -> None:
        """Tests that the function removes all instances of the max value from list"""
        lst: List[int] = [5, 3, 5, 7]
        find_and_remove_max(lst)
        self.assertEqual(lst, [3])

    def test_empty_list(self) -> None:
        """Tests when there is an empty list"""
        lst: List[int] = []
        self.assertEqual(find_and_remove_max(lst), -1)
        self.assertEqual(lst, [])  # The list should remain unchanged

    def test_single_element_list(self) -> None:
        """Tests a list that only contains one element"""
        lst: List[int] = [10]
        self.assertEqual(find_and_remove_max(lst), 10)
        self.assertEqual(
            lst, []
        )  # The list should be empty after removing the single max value


if __name__ == "__main__":
    unittest.main()
