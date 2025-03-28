from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def flattenBoard(self, board: List[List[int]]) -> int:
        flatten = []
        for i, line in enumerate(reversed(board), 0):
            if i % 2 == 0:
                flatten += line
            else:
                flatten += reversed(line)
        return flatten

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        You are given an n x n integer matrix board where the cells are labeled from 1
        to n2 in a Boustrophedon style starting from the bottom left of the board
        (i.e. board[n - 1][0]) and alternating direction each row.

        You start on square 1 of the board. In each move, starting from square curr,
        do the following:
        - Choose a destination square next with a label in the range
        [curr + 1, min(curr + 6, n2)].
        -  This choice simulates the result of a standard 6-sided die roll: i.e., there
        are always at most 6 destinations, regardless of the size of the board.
        - If next has a snake or ladder, you must move to the destination of that snake
        or ladder. Otherwise, you move to next.
        - The game ends when you reach the square n2.

        A board square on row r and column c has a snake or ladder if board[r][c] != -1.
        The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not
        the starting points of any snake or ladder.

        Note that you only take a snake or ladder at most once per dice roll. If the
        destination to a snake or ladder is the start of another snake or ladder, you do
        not follow the subsequent snake or ladder.
        - For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your
        destination square is 2. You follow the ladder to square 3, but do not follow
        the subsequent ladder to 4.

        Return the least number of dice rolls required to reach the square n2. If it is
        not possible to reach the square, return -1.
        """
        board = self.flattenBoard(board)

        def bfs(src, target) -> int:
            def neighbors(pos: int) -> List[int]:
                return [
                    next_pos if board[next_pos] == -1 else board[next_pos] - 1
                    for next_pos in range(pos + 1, min(pos + 7, len(board)))
                ]

            queue = [(src, 0)]
            visited = {src}
            while queue:
                pos, rolls = queue.pop(0)
                if pos == target:
                    return rolls
                for next_pos in neighbors(pos):
                    if next_pos not in visited:
                        queue.append((next_pos, rolls + 1))
                        visited.add(next_pos)
            return -1

        return bfs(0, len(board) - 1)
