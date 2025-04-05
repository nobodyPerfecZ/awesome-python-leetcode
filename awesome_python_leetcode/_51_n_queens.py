from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard
        such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle. You
        may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens'
        placement, where 'Q' and '.' both indicate a queen and an empty space,
        respectively.
        """
        res = []
        cols, diags, anti_diags = set(), set(), set()

        def dfs(row: int, pairs: List[str]):
            if row == n:
                res.append(pairs.copy())
                return
            for col in range(n):
                if col in cols or (row + col) in diags or (row - col) in anti_diags:
                    continue
                cols.add(col)
                diags.add(row + col)
                anti_diags.add(row - col)
                pairs.append(col * "." + "Q" + (n - col - 1) * ".")
                dfs(row + 1, pairs)
                pairs.pop()
                cols.remove(col)
                diags.remove(row + col)
                anti_diags.remove(row - col)

        dfs(0, [])
        return res
