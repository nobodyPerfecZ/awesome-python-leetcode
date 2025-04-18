from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears twice except for
        one. Find that single one.

        You must implement a solution with a linear runtime complexity and use only
        constant extra space.
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res
