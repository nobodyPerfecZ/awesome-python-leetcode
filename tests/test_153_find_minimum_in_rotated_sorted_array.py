from typing import List

import pytest

from awesome_python_leetcode._153_find_minimum_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([5, 1, 2, 3, 4], 1),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    min_val = Solution().findMin(nums)
    assert min_val == expected
