from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on
        the ith day, and an integer fee representing a transaction fee.

        Find the maximum profit you can achieve. You may complete as many transactions
        as you like, but you need to pay the transaction fee for each transaction.

        Note:
        - You may not engage in multiple transactions simultaneously (i.e., you must
        sell the stock before you buy again).
        - The transaction fee is only charged once for each stock purchase and sale.
        """
        dp = {}

        def dfs(i: int, buy: bool):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                # Case: Either BUY or SKIP
                dp[(i, buy)] = max(
                    dfs(i + 1, not buy) - prices[i],  # BUY
                    dfs(i + 1, buy),  # SKIP
                )
            else:
                # Case: Either SELL or SKIP
                dp[(i, buy)] = max(
                    dfs(i + 1, not buy) + prices[i] - fee,  # SELL
                    dfs(i + 1, buy),  # SKIP
                )
            return dp[(i, buy)]

        return dfs(0, True)
