class Solution:
    """Base class for all LeetCode Problems."""

    def numTrees(self, n: int) -> int:
        """
        Given an integer n, return the number of structurally unique BST's
        (binary search trees) which has exactly n nodes of unique values from 1 to n.
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            for k in range((i + 1) // 2):
                if k == 0:
                    dp[i] += dp[i - k - 1]
                else:
                    dp[i] += dp[i - k - 1] * dp[k - 1]
            dp[i] *= 2
            if (i + 1) % 2:
                dp[i] += dp[i - ((i + 1) // 2) - 1] ** 2
        return dp[-1]
