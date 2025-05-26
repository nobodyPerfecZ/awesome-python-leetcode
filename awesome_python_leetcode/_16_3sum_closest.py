from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Given an integer array nums of length n and an integer target, find three
        integers in nums such that the sum is closest to target.

        Return the sum of the three integers.

        You may assume that each input would have exactly one solution.
        """
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        nums = sorted(nums)
        closestSum = -float("inf")
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if abs(target - threeSum) < abs(target - closestSum):
                    closestSum = threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
        return closestSum
