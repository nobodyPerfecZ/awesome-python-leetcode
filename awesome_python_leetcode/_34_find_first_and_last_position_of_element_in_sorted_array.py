from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in non-decreasing order, find the
        starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.
        """
        # start position
        found = False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = True
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        start = left

        if not found:
            return [-1, -1]

        # end position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        end = right

        return [start, end]
