from typing import List

import pytest

from awesome_python_leetcode._2144_minimum_cost_of_buying_candies_with_discount import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["cost", "expected"],
    argvalues=[
        ([1, 2, 3], 5),
        ([6, 5, 7, 9, 2, 2], 23),
        ([5, 5], 10),
    ],
)
def test_func(cost: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().minimumCost(cost)
    assert two_sum == expected
