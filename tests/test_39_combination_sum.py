from typing import List

import pytest

from awesome_python_leetcode._39_combination_sum import Solution


@pytest.mark.parametrize(
    argnames=["candidates", "target", "expected"],
    argvalues=[
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ],
)
def test_func(candidates: List[int], target: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().combinationSum(candidates, target)
    assert combinations == expected
