class Solution:
    """Base class for all LeetCode Problems."""

    def fibTD(self, n: int) -> int:
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
        Fibonacci sequence, such that each number is the sum of the two preceding ones,
        starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.

        Given n, calculate F(n).
        """
        # Top-Down Dynamic Programming (Memoization)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        dp = {}

        def dfs(m: int) -> int:
            if m == 0:
                return 0
            elif m == 1:
                return 1
            elif m in dp:
                return dp[m]
            else:
                dp[m - 1] = dfs(m - 1)
                dp[m - 2] = dfs(m - 2)
                dp[m] = dp[m - 1] + dp[m - 2]
                return dp[m]

        return dfs(n)

    def fibBU(self, n: int) -> int:
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
        Fibonacci sequence, such that each number is the sum of the two preceding ones,
        starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.

        Given n, calculate F(n).
        """
        # Bottom-Up Dynamic Programming (Tabulation)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
