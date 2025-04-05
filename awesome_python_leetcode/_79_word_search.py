from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word
        exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where
        adjacent cells are horizontally or vertically neighboring. The same letter cell
        may not be used more than once.
        """
        path = set()

        def dfs(row: int, col: int, i: int):
            if i == len(word):
                return True
            if (
                row < 0
                or row >= len(board)
                or col < 0
                or col >= len(board[0])
                or board[row][col] != word[i]
                or (row, col) in path
            ):
                return False
            path.add((row, col))
            res = (
                dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            path.remove((row, col))
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False
