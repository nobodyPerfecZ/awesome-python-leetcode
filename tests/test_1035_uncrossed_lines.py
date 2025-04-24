from typing import List

import pytest

from awesome_python_leetcode._1035_uncrossed_lines import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "nums2", "expected"],
    argvalues=[
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ],
)
def test_func(nums1: List[int], nums2: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_crossed_lines = Solution().maxUncrossedLines(nums1, nums2)
    assert max_crossed_lines == expected
