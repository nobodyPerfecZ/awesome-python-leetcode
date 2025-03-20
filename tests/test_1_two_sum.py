from typing import List

import pytest

from awesome_python_leetcode._1_two_sum import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_func(nums: List[int], target: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().twoSum(nums, target)
    assert two_sum == expected
