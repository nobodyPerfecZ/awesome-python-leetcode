from typing import List

import pytest

from awesome_python_leetcode._215_kth_largest_element_in_an_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([2, 1], 1, 2),
    ],
)
def test_func(nums: List[int], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    largest = Solution().findKthLargest(nums, k)
    assert largest == expected
