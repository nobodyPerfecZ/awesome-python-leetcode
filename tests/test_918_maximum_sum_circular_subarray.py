from typing import List

import pytest

from awesome_python_leetcode._918_maximum_sum_circular_subarray import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
        ([-3, -2, -3], -2),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    maxSum = Solution().maxSubarraySumCircular(nums)
    assert maxSum == expected
