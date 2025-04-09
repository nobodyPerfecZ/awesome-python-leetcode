from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on
        the ith day.

        Find the maximum profit you can achieve. You may complete at most two
        transactions.

        Note: You may not engage in multiple transactions simultaneously (i.e., you
        must sell the stock before you buy again).
        """
        dp = [0 for _ in range(len(prices))]

        for t in range(1, 3):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return profit
