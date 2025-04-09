from typing import List

import pytest

from awesome_python_leetcode._188_best_time_to_buy_and_sell_stock_IV import Solution


@pytest.mark.parametrize(
    argnames=["k", "prices", "expected"],
    argvalues=[
        (2, [2, 4, 1], 2),
        (2, [3, 2, 6, 5, 0, 3], 7),
    ],
)
def test_func(k: int, prices: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    profit = Solution().maxProfit(k, prices)
    assert profit == expected
