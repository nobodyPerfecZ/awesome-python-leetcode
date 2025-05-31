from typing import List

import pytest

from awesome_python_leetcode._18_four_sum import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([-2, -1, -1, 1, 1, 2, 2], 0, [[-2, -1, 1, 2], [-1, -1, 1, 1]]),
    ],
)
def test_func(nums: List[int], target: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    four_sums = Solution().fourSum(nums, target)
    assert four_sums == expected
