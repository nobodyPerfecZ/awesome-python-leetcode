class Solution:
    """Base class for all LeetCode Problems."""

    def totalNQueens(self, n: int) -> int:
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard
        such that no two queens attack each other.

        Given an integer n, return the number of distinct solutions to the n-queens
        puzzle.
        """
        count = 0
        cols, diags, anti_diags = set(), set(), set()

        def dfs(row: int):
            if row == n:
                nonlocal count
                count += 1
                return
            for col in range(n):
                if col in cols or (row + col) in diags or (row - col) in anti_diags:
                    continue
                cols.add(col)
                diags.add(row + col)
                anti_diags.add(row - col)
                dfs(row + 1)
                cols.remove(col)
                diags.remove(row + col)
                anti_diags.remove(row - col)

        dfs(0)
        return count
