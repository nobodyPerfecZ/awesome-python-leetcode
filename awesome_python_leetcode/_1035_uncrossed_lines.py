from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        You are given two integer arrays nums1 and nums2. We write the integers of
        nums1 and nums2 (in the order they are given) on two separate horizontal lines.

        We may draw connecting lines: a straight line connecting two numbers nums1[i]
        and nums2[j] such that:
        - nums1[i] == nums2[j], and
        - the line we draw does not intersect any other connecting (non-horizontal)
        line.

        Note that a connecting line cannot intersect even at the endpoints (i.e., each
        number can only belong to one connecting line).

        Return the maximum number of connecting lines we can draw in this way.
        """
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
