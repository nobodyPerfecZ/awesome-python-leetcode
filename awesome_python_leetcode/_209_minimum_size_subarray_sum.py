from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return
        the minimal length of a subarray whose sum is greater than or equal to target.
        If there is no such subarray, return 0 instead.
        """
        curVal, minLen = 0, float("inf")
        left, right = 0, 0
        while left < len(nums) and right < len(nums):
            curVal += nums[right]
            if curVal < target:
                right += 1
            else:
                minLen = min(minLen, right - left + 1)
                curVal -= nums[right]
                curVal -= nums[left]
                left += 1
        return minLen if minLen < float("inf") else 0
