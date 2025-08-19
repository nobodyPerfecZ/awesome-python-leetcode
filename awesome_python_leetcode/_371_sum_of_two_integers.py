class Solution:
    """Base class for all LeetCode Problems."""

    def getSum(self, a: int, b: int) -> int:
        """
        Given two integers a and b, return the sum of the two integers without using
        the operators + and -.
        """
        MASK = 0xFFFFFFFF  # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF  # Max positive 32-bit integer

        a &= MASK
        b &= MASK

        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)
