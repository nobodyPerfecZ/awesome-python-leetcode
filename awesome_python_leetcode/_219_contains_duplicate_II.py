from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if there are
        two distinct indices i and j in the array such that nums[i] == nums[j] and
        abs(i - j) <= k.
        """

        sliding_window = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                sliding_window.remove(nums[left])
                left += 1
            if nums[right] in sliding_window:
                return True
            sliding_window.add(nums[right])
        return False
