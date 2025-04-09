from typing import List

import pytest

from awesome_python_leetcode._123_best_time_to_buy_and_sell_stock_III import Solution


@pytest.mark.parametrize(
    argnames=["prices", "expected"],
    argvalues=[
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_func(prices: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    profit = Solution().maxProfit(prices)
    assert profit == expected
