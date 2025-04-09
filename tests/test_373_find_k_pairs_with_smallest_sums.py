from typing import List

import pytest

from awesome_python_leetcode._373_find_k_pairs_with_smallest_sums import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "nums2", "k", "expected"],
    argvalues=[
        ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
        ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
    ],
)
def test_func(nums1: List[int], nums2: List[int], k: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    pairs = Solution().kSmallestPairs(nums1, nums2, k)
    assert pairs == expected
