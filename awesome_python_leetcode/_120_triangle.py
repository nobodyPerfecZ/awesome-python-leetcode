from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Given a triangle array, return the minimum path sum from top to bottom.

        For each step, you may move to an adjacent number of the row below. More
        formally, if you are on index i on the current row, you may move to either
        index i or index i + 1 on the next row.
        """
        dp = [[float("inf")] * len(layer) for layer in triangle]
        dp[-1] = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
