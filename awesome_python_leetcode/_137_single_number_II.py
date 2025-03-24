from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def singleNumber(self, nums: List[int]) -> int:
        """
        Given an integer array nums where every element appears three times except for
        one, which appears exactly once. Find the single element and return it.

        You must implement a solution with a linear runtime complexity and use only
        constant extra space.
        """
        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones
