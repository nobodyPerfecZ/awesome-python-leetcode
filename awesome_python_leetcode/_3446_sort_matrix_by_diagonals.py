from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        You are given an n x n square matrix of integers grid. Return the matrix such
        that:
        - The diagonals in the bottom-left triangle (including the middle diagonal) are
        sorted in non-increasing order.
        - The diagonals in the top-right triangle are sorted in non-decreasing order.
        """
        # Collect diagonals
        diag = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = i - j
                if key not in diag:
                    diag[key] = []
                diag[key].append(grid[i][j])

        # Sort in decreasing / increasing order for each diagonal
        diag = dict(
            zip(
                diag.keys(),
                map(lambda key: sorted(diag[key], reverse=(key >= 0)), diag.keys()),
                strict=False,
            )
        )

        # Apply the sorted diagonals to the result matrix
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = i - j
                result[i][j] = diag[key].pop(0)

        return result
