class Solution:
    """Base class for all LeetCode Problems."""

    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n != 0:
            n = n // 5
            zeros += n
        return zeros
