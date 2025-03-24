from typing import List

import pytest

from awesome_python_leetcode._122_best_time_to_buy_and_sell_stock_II import Solution


@pytest.mark.parametrize(
    argnames=["prices", "expected"],
    argvalues=[
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_func(prices: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_profit = Solution().maxProfit(prices)
    assert max_profit == expected
