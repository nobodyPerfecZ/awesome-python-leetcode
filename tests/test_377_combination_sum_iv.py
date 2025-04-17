from typing import List

import pytest

from awesome_python_leetcode._377_combination_sum_iv import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
    ],
)
def test_func(nums: List[int], target: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().combinationSum4(nums, target)
    assert combinations == expected
