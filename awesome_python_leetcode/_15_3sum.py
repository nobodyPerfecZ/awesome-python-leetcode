from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets
        [nums[i], nums[j],nums[k]] such that i != j, i != k, and j != k, and
        nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        """
        nums = sorted(nums)
        threeSums = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    threeSums.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
        return threeSums
