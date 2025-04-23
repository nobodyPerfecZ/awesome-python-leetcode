# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._714_best_time_to_buy_and_sell_stock_with_transaction_fee import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["prices", "fee", "expected"],
    argvalues=[
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
    ],
)
def test_func(prices: List[int], fee: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    max_profit = Solution().maxProfit(prices, fee)
    assert max_profit == expected
