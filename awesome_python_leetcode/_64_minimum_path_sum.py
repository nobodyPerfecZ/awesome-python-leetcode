from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Given a m x n grid filled with non-negative numbers, find a path from top left
        to bottom right, which minimizes the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.
        """
        dp = [[0] * len(line) for line in grid]
        dp[0][0] = grid[0][0]
        for j in range(1, len(dp[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
