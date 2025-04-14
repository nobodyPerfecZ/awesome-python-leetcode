from typing import List

import pytest

from awesome_python_leetcode._518_coin_change_II import Solution


@pytest.mark.parametrize(
    argnames=["amount", "coins", "expected"],
    argvalues=[
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
    ],
)
def test_func(amount: int, coins: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().change(amount, coins)
    assert combinations == expected
