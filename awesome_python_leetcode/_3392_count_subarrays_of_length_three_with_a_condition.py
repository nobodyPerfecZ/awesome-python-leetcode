from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def countSubarrays(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the number of subarrays of length 3 such
        that the sum of the first and third numbers equals exactly half of the second
        number.

        A subarray is a contiguous non-empty sequence of elements within an array.
        """
        count = 0
        for i in range(1, len(nums) - 1):
            if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
                count += 1
        return count
