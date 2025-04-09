from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given
        stock on the ith day, and an integer k.

        Find the maximum profit you can achieve. You may complete at most k
        transactions: i.e. you may buy at most k times and sell at most k times.

        Note: You may not engage in multiple transactions simultaneously (i.e., you
        must sell the stock before you buy again).
        """
        dp = [0 for _ in range(len(prices))]

        for t in range(1, k + 1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return profit
