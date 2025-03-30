from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        You are given a large integer represented as an integer array digits, where each
        digits[i] is the ith digit of the integer. The digits are ordered from most
        significant to least significant in left-to-right order. The large integer does
        not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.
        """
        leftover = 1
        for i in range(len(digits) - 1, -1, -1):
            if leftover == 0:
                break
            val = digits[i] + leftover
            digits[i] = val % 10
            leftover = val // 10
        if leftover == 1:
            digits.insert(0, leftover)
        return digits
