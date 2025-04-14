class Solution:
    """Base class for all LeetCode Problems."""

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Given a string s, find the longest palindromic subsequence's length in s.

        A subsequence is a sequence that can be derived from another sequence by
        deleting some or no elements without changing the order of the remaining
        elements.
        """
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[len(s) - 1 - i] == s[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
