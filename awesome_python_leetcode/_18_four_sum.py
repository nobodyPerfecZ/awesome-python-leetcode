from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Given an array nums of n integers, return an array of all the unique quadruplets
        [nums[a], nums[b], nums[c], nums[d]] such that:

        - 0 <= a, b, c, d < n
        - a, b, c, and d are distinct.
        - nums[a] + nums[b] + nums[c] + nums[d] == target

        You may return the answer in any order.
        """
        nums = sorted(nums)
        fourSums = []
        i = 0
        while i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < len(nums) - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        fourSums.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                j += 1
            i += 1
        return fourSums
