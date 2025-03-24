class Solution:
    """Base class for all LeetCode Problems."""

    def reverseBits(self, n: int) -> int:
        """Reverse bits of a given 32 bits unsigned integer."""
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
