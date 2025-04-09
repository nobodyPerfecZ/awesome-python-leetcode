from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        You are given an m x n integer array grid. There is a robot initially located
        at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
        bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
        down or right at any point in time.

        An obstacle and space are marked as 1 or 0 respectively in grid. A path that
        the robot takes cannot include any square that is an obstacle.

        Return the number of possible unique paths that the robot can take to reach the
        bottom-right corner.

        The testcases are generated so that the answer will be less than or equal to
        2 * 109.
        """
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * len(line) for line in obstacleGrid]
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
