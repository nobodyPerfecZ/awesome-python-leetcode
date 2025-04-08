from typing import List

import pytest

from awesome_python_leetcode._322_coin_change import Solution


@pytest.mark.parametrize(
    argnames=["coins", "amount", "expected"],
    argvalues=[
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ],
)
def test_func(coins: List[int], amount: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_coins = Solution().coinChange(coins, amount)
    assert num_coins == expected
