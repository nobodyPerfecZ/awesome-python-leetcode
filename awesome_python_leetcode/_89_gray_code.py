from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def grayCode(self, n: int) -> List[int]:
        """
        An n-bit gray code sequence is a sequence of 2n integers where:
        - Every integer is in the inclusive range [0, 2n - 1],
        - The first integer is 0,
        - An integer appears no more than once in the sequence,
        - The binary representation of every pair of adjacent integers differs by
        exactly one bit, and
        - The binary representation of the first and last integers differs by exactly
        one bit.

        Given an integer n, return any valid n-bit gray code sequence.
        """
        result = []
        total_numbers = 1 << n

        for i in range(total_numbers):
            result.append(i ^ (i >> 1))

        return result
