from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        You are given an integer array nums consisting of n elements, and an integer k.

        Find a contiguous subarray whose length is equal to k that has the maximum
        average value and return this value. Any answer with a calculation error less
        than 10-5 will be accepted.
        """
        max_average = nums[0]
        average = nums[0]
        for left in range(len(nums) - k + 1):
            if left:
                average = average - nums[left - 1] + nums[left + k - 1]
                max_average = max(max_average, average)
            else:
                average = sum(nums[left : left + k])
                max_average = sum(nums[left : left + k])
        return max_average / k
