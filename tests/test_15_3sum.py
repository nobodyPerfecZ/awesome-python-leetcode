from typing import List

import pytest

from awesome_python_leetcode._15_3sum import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_func(nums: List[int], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    three_sum = Solution().threeSum(nums)
    assert three_sum == expected
