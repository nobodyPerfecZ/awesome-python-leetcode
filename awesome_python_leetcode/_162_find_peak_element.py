from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findPeakElement(self, nums: List[int]) -> int:
        """
        A peak element is an element that is strictly greater than its neighbors.

        Given a 0-indexed integer array nums, find a peak element, and return its index.
        If the array contains multiple peaks, return the index to any of the peaks.

        You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
        always considered to be strictly greater than a neighbor that is outside the
        array.

        You must write an algorithm that runs in O(log n) time.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            leftVal = -float("inf") if mid == 0 else nums[mid - 1]
            rightVal = -float("inf") if mid == len(nums) - 1 else nums[mid + 1]

            if leftVal < midVal and rightVal < midVal:
                return mid
            elif rightVal > midVal:
                left = mid + 1
            elif leftVal > midVal:
                right = mid - 1

        return -1
