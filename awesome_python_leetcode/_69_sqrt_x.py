class Solution:
    """Base class for all LeetCode Problems."""

    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, return the square root of x rounded down to the
        nearest integer. The returned integer should be non-negative as well.

        You must not use any built-in exponent function or operator.
        - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
        """
        left, right = 0, x
        res = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
                res = mid
            else:
                return mid
        return res
