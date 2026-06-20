class Solution:
    """Base class for all LeetCode Problems."""

    def divide(self, dividend: int, divisor: int) -> int:
        """
        Given two integers dividend and divisor, divide two integers without
        using multiplication, division, and mod operator.

        The integer division should truncate toward zero, which means losing its
        fractional part. For example, 8.345 would be truncated to 8, and
        -2.7335 would be truncated to -2.

        Return the quotient after dividing dividend by divisor.

        Note: Assume we are dealing with an environment that could only store
        integers within the 32-bit signed integer range: [−231, 231 − 1]. For
        this problem, if the quotient is strictly greater than 231 - 1, then
        return 231 - 1, and if the quotient is strictly less than -231, then
        return -231.
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        c = 0
        flag = 0
        if dividend < 0 and divisor < 0:
            flag = 0
        elif dividend < 0 or divisor < 0:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            t_divisor = divisor
            multiple = 1
            while dividend >= (t_divisor << 1):
                t_divisor <<= 1
                multiple <<= 1
            dividend = dividend - t_divisor
            c = c + multiple
        if flag == 1:
            return c * -1
        else:
            return c
