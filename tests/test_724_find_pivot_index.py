from typing import List

import pytest

from awesome_python_leetcode._724_find_pivot_index import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    pivot_idx = Solution().pivotIndex(nums)
    assert pivot_idx == expected
