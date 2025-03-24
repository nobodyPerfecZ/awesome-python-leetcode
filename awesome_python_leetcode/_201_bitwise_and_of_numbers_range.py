class Solution:
    """Base class for all LeetCode Problems."""

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Given two integers left and right that represent the range [left, right],
        return the bitwise AND of all numbers in this range, inclusive.
        """
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i
