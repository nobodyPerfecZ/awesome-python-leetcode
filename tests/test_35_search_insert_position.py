from typing import List

import pytest

from awesome_python_leetcode._35_search_insert_position import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_func(nums: List[int], target: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    idx = Solution().searchInsert(nums, target)
    assert idx == expected
