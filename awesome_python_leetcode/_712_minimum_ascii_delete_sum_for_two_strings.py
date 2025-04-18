class Solution:
    """Base class for all LeetCode Problems."""

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Given two strings s1 and s2, return the lowest ASCII sum of deleted characters
        to make two strings equal.
        """
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1]
                    )
        return dp[-1][-1]
