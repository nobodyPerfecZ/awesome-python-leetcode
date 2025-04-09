from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Given an m x n binary matrix filled with 0's and 1's, find the largest square
        containing only 1's and return its area.
        """
        dp = [[0 for _ in line] for line in matrix]
        maxArea = 0

        for i in range(len(matrix) - 1, -1, -1):
            dp[i][-1] = int(matrix[i][-1])
            maxArea = max(maxArea, dp[i][-1])

        for j in range(len(matrix[0]) - 1, -1, -1):
            dp[-1][j] = int(matrix[-1][j])
            maxArea = max(maxArea, dp[-1][j])

        for i in range(len(matrix) - 2, -1, -1):
            for j in range(len(matrix[0]) - 2, -1, -1):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                maxArea = max(maxArea, dp[i][j])
        return maxArea**2
