class Solution:
    """Base class for all LeetCode Problems."""

    def hammingWeight(self, n: int) -> int:
        """
        Given a positive integer n, write a function that returns the number of set bits
        in its binary representation (also known as the Hamming weight).
        """
        count = 0
        for i in range(32):
            if (n >> i) & 1:
                count += 1
        return count
