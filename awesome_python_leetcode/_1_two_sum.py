from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the
        two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not
        use the same element twice.

        You can return the answer in any order.
        """
        values = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in values:
                return [values[diff], i]
            values[n] = i
        return
