class Solution:
    """Base class for all LeetCode Problems."""

    def minInsertions(self, s: str) -> int:
        """
        Given a string s. In one step you can insert any character at any index of the
        string.

        Return the minimum number of steps to make s palindrome.

        A Palindrome String is one that reads the same backward as well as forward.
        """
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == s[len(s) - 1 - j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return len(s) - dp[0][0]
