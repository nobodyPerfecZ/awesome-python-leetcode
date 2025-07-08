from typing import List

import pytest

from awesome_python_leetcode._2215_find_the_difference_of_two_arrays import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "nums2", "expected"],
    argvalues=[
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ],
)
def test_func(nums1: List[int], nums2: List[int], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    diff = Solution().findDifference(nums1, nums2)
    assert diff == expected
