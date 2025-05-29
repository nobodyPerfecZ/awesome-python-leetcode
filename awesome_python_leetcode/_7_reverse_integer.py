class Solution:
    """Base class for all LeetCode Problems."""

    def reverse(self, x: int) -> int:
        """
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing
        x causes the value to go outside the signed 32-bit integer range
        [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers
        (signed or unsigned).
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        sign = "-" if x < 0 else "+"
        x = abs(x)
        result = 0
        while x != 0:
            # Check if 32-bit integer
            if sign == "-" and result >= (2**31) / 10:
                return 0
            if sign == "+" and result >= (2**31 - 1) / 10:
                return 0

            digit = x % 10
            result *= 10
            result += digit
            x = x // 10

        return -result if sign == "-" else result
