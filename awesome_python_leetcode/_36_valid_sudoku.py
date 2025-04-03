import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
        validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
        without repetition.

        Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily
        solvable.
        - Only the filled cells need to be validated according to the mentioned rules.
        """
        rows, cols, squares = (
            collections.defaultdict(set),
            collections.defaultdict(set),
            collections.defaultdict(set),
        )

        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num == ".":
                    continue
                rowIdx = row
                colIdx = col
                squareIdx = 3 * (row // 3) + col // 3

                if (
                    num in rows[rowIdx]
                    or num in cols[colIdx]
                    or num in squares[squareIdx]
                ):
                    return False

                rows[rowIdx].add(num)
                cols[colIdx].add(num)
                squares[squareIdx].add(num)
        return True
