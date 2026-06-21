from typing import List

import pytest

from awesome_python_leetcode._40_combination_sum_II import Solution


@pytest.mark.parametrize(
    argnames=["candidates", "target", "expected"],
    argvalues=[
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ],
)
def test_func(candidates: List[int], target: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    combination_sum_2 = Solution().combinationSum2(candidates, target)
    assert combination_sum_2 == expected
