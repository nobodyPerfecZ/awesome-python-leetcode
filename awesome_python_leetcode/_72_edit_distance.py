class Solution:
    """Base class for all LeetCode Problems."""

    def minDistance(self, word1: str, word2: str) -> int:
        """
        Given two strings word1 and word2, return the minimum number of operations
        required to convert word1 to word2.

        You have the following three operations permitted on a word:
        - Insert a character
        - Delete a character
        - Replace a character
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) - 1, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + 1

        for j in range(len(word2) - 1, -1, -1):
            dp[-1][j] = dp[-1][j + 1] + 1

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
