class Solution:
    """Base class for all LeetCode Problems."""

    def tribonacci(self, n: int) -> int:
        """
        The Tribonacci sequence Tn is defined as follows:

        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        Given n, return the value of Tn.
        """
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]
