class Solution:
    """Base class for all LeetCode Problems."""

    def findComplement(self, num: int) -> int:
        """
        The complement of an integer is the integer you get when you flip all the 0's
        to 1's and all the 1's to 0's in its binary representation.
        - For example, The integer 5 is "101" in binary and its complement is "010"
        which is the integer 2.

        Given an integer num, return its complement.
        """
        if num == 0:
            return 1

        res = 0
        i = 0
        while num != 0:
            bit = num & 1
            res += (bit ^ 1) << i
            num >>= 1
            i += 1
        return res
