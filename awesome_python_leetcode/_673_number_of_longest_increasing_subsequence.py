from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the number of longest increasing
        subsequences.

        Notice that the sequence has to be strictly increasing.
        """
        dp = {}
        lenLIS, res = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
        return res
