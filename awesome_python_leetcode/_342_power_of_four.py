class Solution:
    """Base class for all LeetCode Problems."""

    def isPowerOfFour(self, n: int) -> bool:
        """
        Given an integer n, return true if it is a power of four.
        Otherwise, return false.

        An integer n is a power of four, if there exists an integer x such that n == 4x.
        """
        x = n
        count_ones = 0
        while x > 0:
            count_ones += x & 1
            x >>= 1
        return (count_ones == 1) & (n.bit_length() % 2 == 1)
