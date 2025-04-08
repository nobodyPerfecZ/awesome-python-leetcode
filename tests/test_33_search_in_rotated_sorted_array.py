from typing import List

import pytest

from awesome_python_leetcode._33_search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ],
)
def test_func(nums: List[int], target: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    idx = Solution().search(nums, target)
    assert idx == expected
