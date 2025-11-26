from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def numberOfPathsTD(self, grid: List[List[int]], k: int) -> int:
        """
        You are given a 0-indexed m x n integer matrix grid and an integer k.
        You are currently at position (0, 0) and you want to reach position
        (m - 1, n - 1) moving only down or right.

        Return the number of paths where the sum of the elements on the path is
        divisible by k. Since the answer may be very large, return it modulo 109 + 7.
        """
        # Top-Down Dynamic Programming (Memoization)
        ROWS = len(grid)
        COLS = len(grid[0])
        MOD = 10**9 + 7
        dp = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row: int, col: int, remain: int):
            if row == ROWS - 1 and col == COLS - 1:
                remain = (grid[row][col] + remain) % k
                return 0 if remain else 1
            if row == ROWS or col == COLS:
                return 0
            if dp[row][col][remain] > -1:
                return dp[row][col][remain]
            dp[row][col][remain] = (
                dfs(row + 1, col, (grid[row][col] + remain) % k) % MOD
                + dfs(row, col + 1, (grid[row][col] + remain) % k) % MOD
            ) % MOD
            return dp[row][col][remain]

        return dfs(0, 0, 0)

    def numberOfPathsBU(self, grid: List[List[int]], k: int) -> int:
        """
        You are given a 0-indexed m x n integer matrix grid and an integer k.
        You are currently at position (0, 0) and you want to reach position
        (m - 1, n - 1) moving only down or right.

        Return the number of paths where the sum of the elements on the path is
        divisible by k. Since the answer may be very large, return it modulo 109 + 7.
        """
        # Bottom-Up Dynamic Programming (Tabulation)
        ROWS = len(grid)
        COLS = len(grid[0])
        MOD = 10**9 + 7
        dp = [[[0] * k for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        target_remain = (k - (grid[ROWS - 1][COLS - 1] % k)) % k
        dp[ROWS - 1][COLS - 1][target_remain] = 1

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if row == ROWS - 1 and col == COLS - 1:
                    continue
                for remain in range(k):
                    new_remain = (grid[row][col] + remain) % k
                    dp[row][col][remain] = (
                        dp[row + 1][col][new_remain] % MOD
                        + dp[row][col + 1][new_remain] % MOD
                    ) % MOD

        return dp[0][0][0]
