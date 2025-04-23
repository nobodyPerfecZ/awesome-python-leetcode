from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on
        the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions
        as you like (i.e., buy one and sell one share of the stock multiple times) with
        the following restrictions:
        - After you sell your stock, you cannot buy stock on the next day
        (i.e., cooldown one day).

        Note: You may not engage in multiple transactions simultaneously (i.e., you
        must sell the stock before you buy again).
        """
        dp = {}

        def dfs(i: int, buy: bool):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                # Case: Either BUY or COOLDOWN
                dp[(i, buy)] = max(
                    dfs(i + 1, not buy) - prices[i],  # BUY
                    dfs(i + 1, buy),  # COOLDOWN
                )
            else:
                # Case: Either SELL + COOLDOWN or COOLDOWN
                dp[(i, buy)] = max(
                    dfs(i + 2, not buy) + prices[i],  # SELL + COOLDOWN
                    dfs(i + 1, buy),  # COOLDOWN
                )
            return dp[(i, buy)]

        return dfs(0, True)
