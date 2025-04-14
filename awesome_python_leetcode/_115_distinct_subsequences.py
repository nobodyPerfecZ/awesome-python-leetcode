class Solution:
    """Base class for all LeetCode Problems."""

    def numDistinct(self, s: str, t: str) -> int:
        """
        Given two strings s and t, return the number of distinct subsequences of s
        which equals t.

        The test cases are generated so that the answer fits on a 32-bit signed
        integer.
        """
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
