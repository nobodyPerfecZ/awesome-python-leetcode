class Solution:
    """Base class for all LeetCode Problems."""

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Given an integer n, return true if it is a power of two.
        Otherwise, return false.

        An integer n is a power of two, if there exists an integer x such that n == 2x.
        """
        num_ones = 0
        while n > 0:
            num_ones += n & 1  # Get the last bit
            n >>= 1  # shift right
        return num_ones == 1
