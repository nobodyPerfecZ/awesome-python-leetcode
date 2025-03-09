from typing import List

import pytest

from awesome_python_leetcode._121_best_time_to_buy_and_sell_stocks import Solution


@pytest.mark.parametrize(
    argnames=["prices", "expected"],
    argvalues=[
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_func(prices: List[int], expected: int):
    max_profit = Solution().maxProfit(prices)
    assert max_profit == expected
