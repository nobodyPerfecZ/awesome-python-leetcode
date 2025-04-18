from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index
        if the target is found. If not, return the index where it would be if it were
        inserted in order.

        You must write an algorithm with O(log n) runtime complexity.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
