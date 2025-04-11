from typing import List

import pytest

from awesome_python_leetcode._746_min_cost_climbing_stairs import Solution


@pytest.mark.parametrize(
    argnames=["cost", "expected"],
    argvalues=[
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ],
)
def test_func(cost: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    min_cost = Solution().minCostClimbingStairs(cost)
    assert min_cost == expected
