from typing import List

import pytest

from awesome_python_leetcode._309_best_time_to_buy_and_sell_stock_with_cooldown import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["prices", "expected"],
    argvalues=[
        ([1, 2, 3, 0, 2], 3),
        ([1], 0),
    ],
)
def test_func(prices: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_profit = Solution().maxProfit(prices)
    assert max_profit == expected
