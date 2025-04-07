from typing import List

import pytest

from awesome_python_leetcode._53_maximum_subarray import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    maxSum = Solution().maxSubArray(nums)
    assert maxSum == expected
