from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, in which exactly two elements appear only once and
        all the other elements appear exactly twice. Find the two elements that appear
        only once. You can return the answer in any order.

        You must write an algorithm that runs in linear runtime complexity and uses
        only constant extra space.
        """
        # Get the XOR product of the two distinct values
        result = 0
        for n in nums:
            result ^= n

        # Get the position of the first 1-bit
        k = 0
        while result & 1 == 0:
            result >>= 1
            k += 1

        # Group the values according to the first 1-bit
        num1, num2 = 0, 0
        for n in nums:
            if (n & (1 << k)) >> k == 1:
                num1 ^= n
            else:
                num2 ^= n

        return [num1, num2]
