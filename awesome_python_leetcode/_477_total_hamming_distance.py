from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        The Hamming distance between two integers is the number of positions at which
        the corresponding bits are different.

        Given an integer array nums, return the sum of Hamming distances between all the
        pairs of the integers in nums.
        """
        result = 0
        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            zeros = len(nums) - ones
            result += ones * zeros
        return result
