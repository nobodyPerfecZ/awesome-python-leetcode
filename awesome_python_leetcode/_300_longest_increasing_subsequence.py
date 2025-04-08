from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.

        A subsequence is an array that can be derived from another array by deleting
        some or no elements without changing the order of the remaining elements.
        """
        dp = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
