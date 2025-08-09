class Solution:
    """Base class for all LeetCode Problems."""

    def hammingDistance(self, x: int, y: int) -> int:
        """
        The Hamming distance between two integers is the number of positions at which
        the corresponding bits are different.

        Given two integers x and y, return the Hamming distance between them.
        """
        distance = 0
        while x > 0 or y > 0:
            # Get the last bit
            distance += (x & 1) ^ (y & 1)

            # Shift to the right
            x >>= 1
            y >>= 1
        return distance
