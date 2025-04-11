from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Given an integer numRows, return the first numRows of Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers directly above
        it as shown:
        numRows = 5
        Output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
        ]
        """
        dp = [[1 for _ in range(i)] for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp
