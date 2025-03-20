from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on
        the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and
        choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot
        achieve any profit, return 0.
        """
        left, right, best_profit = 0, 1, 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                if profit > best_profit:
                    best_profit = profit
                right += 1
        return best_profit
