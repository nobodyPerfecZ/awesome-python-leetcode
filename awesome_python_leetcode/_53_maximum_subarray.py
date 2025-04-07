from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray with the largest sum, and return
        its sum.
        """
        maxSum, curSum = -float("inf"), -float("inf")
        for i in range(len(nums)):
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
        return maxSum
