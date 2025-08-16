from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        We have two special characters:
        - The first character can be represented by one bit 0.
        - The second character can be represented by two bits (10 or 11).

        Given a binary array bits that ends with 0, return true if the last character
        must be a one-bit character.
        """
        i = 0
        while i < len(bits):
            if i == len(bits) - 2 and bits[i] == 1:
                return False
            if bits[i] == 1:
                i += 1
            i += 1
        return True
