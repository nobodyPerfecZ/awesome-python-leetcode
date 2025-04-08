from typing import List

import pytest

from awesome_python_leetcode._4_median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "nums2", "expected"],
    argvalues=[
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ],
)
def test_func(nums1: List[int], nums2: List[int], expected: float):
    """Tests the solution of a LeetCode problem."""
    median = Solution().findMedianSortedArrays(nums1, nums2)
    assert median == expected
