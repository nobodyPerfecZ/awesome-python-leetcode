from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def change(self, amount: int, coins: List[int]) -> int:
        """
        You are given an integer array coins representing coins of different
        denominations and an integer amount representing a total amount of money.

        Return the number of combinations that make up that amount. If that amount of
        money cannot be made up by any combination of the coins, return 0.

        You may assume that you have an infinite number of each kind of coin.

        The answer is guaranteed to fit into a signed 32-bit integer.
        """
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        dp[0] = [1 for _ in range(len(coins) + 1)]

        for i in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j]
        return dp[amount][0]
