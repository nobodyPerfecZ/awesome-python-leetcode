# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._34_find_first_and_last_position_of_element_in_sorted_array import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ],
)
def test_func(nums: List[int], target: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    ranges = Solution().searchRange(nums, target)
    assert ranges == expected
