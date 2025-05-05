from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Write a program to solve a Sudoku puzzle by filling the empty cells.

        A sudoku solution must satisfy all of the following rules:
        1. Each of the digits 1-9 must occur exactly once in each row.
        2. Each of the digits 1-9 must occur exactly once in each column.
        3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
        sub-boxes of the grid.

        The '.' character indicates empty cells.
        """
        # Time complexity: O(9^81)
        # Space complexity: O(9^81)
        # Compute remaining rows, cols and squares
        rows = {i: set([str(val) for val in range(1, 10)]) for i in range(0, 9)}
        cols = {i: set([str(val) for val in range(1, 10)]) for i in range(0, 9)}
        squares = {i: set([str(val) for val in range(1, 10)]) for i in range(0, 9)}
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                square = 3 * (row // 3) + col // 3
                rows[row].remove(board[row][col])
                cols[col].remove(board[row][col])
                squares[square].remove(board[row][col])

        def dfs(row: int, col: int) -> bool:
            new_col = (col + 1) % 9
            new_row = row + 1 if new_col == 0 else row
            if row >= 9:
                return True
            if board[row][col] != ".":
                return dfs(new_row, new_col)
            square = 3 * (row // 3) + col // 3
            visited = rows[row].intersection(cols[col], squares[square])
            for val in visited:
                board[row][col] = val
                rows[row].remove(val)
                cols[col].remove(val)
                squares[square].remove(val)
                if dfs(new_row, new_col):
                    return True
                board[row][col] = "."
                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)
            return False

        return dfs(0, 0)
