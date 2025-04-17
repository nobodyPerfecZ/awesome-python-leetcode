from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        You have planned some train traveling one year in advance. The days of the year
        in which you will travel are given as an integer array days. Each day is an
        integer from 1 to 365.

        Train tickets are sold in three different ways:
        - a 1-day pass is sold for costs[0] dollars,
        - a 7-day pass is sold for costs[1] dollars, and
        - a 30-day pass is sold for costs[2] dollars.

        The passes allow that many days of consecutive travel.
        - For example, if we get a 7-day pass on day 2, then we can travel for 7
        days: 2, 3, 4, 5, 6, 7, and 8.

        Return the minimum number of dollars you need to travel every day in the given
        list of days.
        """
        dp = [0 for i in range(len(days) + 1)]
        for i in range(len(days) - 1, -1, -1):
            j = i + 1
            while j < len(days) and days[i] + 7 > days[j]:
                j += 1
            k = i + 1
            while k < len(days) and days[i] + 30 > days[k]:
                k += 1
            dp[i] = min(costs[0] + dp[i + 1], costs[1] + dp[j], costs[2] + dp[k])
        return dp[0]
