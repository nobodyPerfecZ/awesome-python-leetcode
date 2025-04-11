from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Given an n x n array of integers matrix, return the minimum sum of any falling
        path through matrix.

        A falling path starts at any element in the first row and chooses the element
        in the next row that is either directly below or diagonally left/right.
        Specifically, the next element from position (row, col) will be
        (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
        """
        dp = [
            [matrix[i][j] if i == 0 else 0 for j in range(len(matrix[i]))]
            for i in range(len(matrix))
        ]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == len(matrix[i]) - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
                else:
                    dp[i][j] = (
                        min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                        + matrix[i][j]
                    )
        return min(dp[-1])
