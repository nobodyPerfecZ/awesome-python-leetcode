class Solution:
    """Base class for all LeetCode Problems."""

    def toHex(self, num: int) -> str:
        """
        Given a 32-bit integer num, return a string representing its hexadecimal
        representation. For negative integers, two’s complement method is used.

        All the letters in the answer string should be lowercase characters, and there
        should not be any leading zeros in the answer except for the zero itself.

        Note: You are not allowed to use any built-in library method to directly solve
        this problem.
        """
        if num == 0:
            return "0"

        WRAPPER = "0123456789abcdef"
        MASK = 0xFFFFFFFF
        num &= MASK

        result = ""
        while num != 0:
            bits = num % 16
            result = WRAPPER[bits] + result
            num //= 16
        return result
