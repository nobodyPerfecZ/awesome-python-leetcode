from typing import List

import pytest

from awesome_python_leetcode._88_merge_sorted_array import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "m", "nums2", "n", "expected"],
    argvalues=[
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_func(nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected
