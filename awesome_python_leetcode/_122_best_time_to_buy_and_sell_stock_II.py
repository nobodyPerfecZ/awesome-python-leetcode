from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given
        stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at
        most one share of the stock at any time. However, you can buy it then
        immediately sell it on the same day.

        Find and return the maximum profit you can achieve.
        """
        left, right, best_profit = 0, 1, 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            elif prices[right] - prices[left] > 0:
                best_profit += prices[right] - prices[left]
                left = right
                right += 1
            else:
                right += 1
        return best_profit
