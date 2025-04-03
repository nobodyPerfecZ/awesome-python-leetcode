from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        According to Wikipedia's article: "The Game of Life, also known simply as Life,
        is a cellular automaton devised by the British mathematician John Horton
        Conway in 1970."

        The board is made up of an m x n grid of cells, where each cell has an initial
        state: live (represented by a 1) or dead (represented by a 0). Each cell
        interacts with its eight neighbors (horizontal, vertical, diagonal) using the
        following four rules (taken from the above Wikipedia article):
        1. Any live cell with fewer than two live neighbors dies as if caused by
        under-population.
        2. Any live cell with two or three live neighbors lives on to the next
        generation.
        3. Any live cell with more than three live neighbors dies, as if by
        over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if
        by reproduction.

        The next state of the board is determined by applying the above rules
        simultaneously to every cell in the current state of the m x n grid board. In
        this process, births and deaths occur simultaneously.

        Given the current state of the board, update the board to reflect its next
        state.

        Note that you do not need to return anything.
        """

        def kernel(row: int, col: int) -> int:
            live = board[row][col] == 1
            neighbors = [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]
            sumNeighbors = sum(
                [
                    (
                        board[i_][j_] == 1 or board[i_][j_] == 3
                        if i_ >= 0
                        and i_ < len(board)
                        and j_ >= 0
                        and j_ < len(board[0])
                        else 0
                    )
                    for (i_, j_) in neighbors
                ]
            )
            if live:
                if sumNeighbors < 2 or sumNeighbors > 3:
                    return 1
                else:
                    return 3
            else:
                if sumNeighbors == 3:
                    return 2
                else:
                    return 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = kernel(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] == 2 or board[row][col] == 3:
                    board[row][col] = 1
