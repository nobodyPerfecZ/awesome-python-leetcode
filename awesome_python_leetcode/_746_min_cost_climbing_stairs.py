from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        You are given an integer array cost where cost[i] is the cost of ith step on a
        staircase. Once you pay the cost, you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.

        Return the minimum cost to reach the top of the floor.
        """
        dp = [0 for _ in range(len(cost))]
        for i in range(len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])
