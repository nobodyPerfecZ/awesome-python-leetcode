class Solution:
    """Base class for all LeetCode Problems."""

    def numTilings(self, n: int) -> int:
        """
        You have two types of tiles: a 2 x 1 domino shape and a tromino shape.
        You may rotate these shapes.

        Given an integer n, return the number of ways to tile an 2 x n board.
        Since the answer may be very large, return it modulo 109 + 7.

        In a tiling, every square must be covered by a tile.
        Two tilings are different if and only if there are two 4-directionally adjacent
        cells on the board such that exactly one of the tilings has both squares
        occupied by a tile.
        """
        F = [0 for _ in range(n + 1)]
        F[0], F[1] = 1, 1
        T = [0 for _ in range(n + 1)]
        B = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]
            T[i] = B[i - 1] + F[i - 2]
            B[i] = T[i - 1] + F[i - 2]
        return F[-1] % (10**9 + 7)
