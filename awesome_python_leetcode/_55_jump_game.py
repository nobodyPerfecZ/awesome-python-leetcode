from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at the array's
        first index, and each element in the array represents your maximum jump length
        at that position.

        Return true if you can reach the last index, or false otherwise.
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
