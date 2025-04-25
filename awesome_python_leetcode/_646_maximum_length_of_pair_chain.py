from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
        lefti < righti.

        A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be
        formed in this fashion.

        Return the length longest chain which can be formed.

        You do not need to use up all the given intervals. You can select pairs in any
        order.
        """
        pairs = sorted(pairs)
        dp = [1 for _ in range(len(pairs))]
        for i in range(len(pairs) - 2, -1, -1):
            for j in range(i + 1, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
