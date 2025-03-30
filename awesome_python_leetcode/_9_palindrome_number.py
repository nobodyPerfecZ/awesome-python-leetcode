from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def digits(self, x: int) -> List[int]:
        x = abs(x)
        digits = []
        while x != 0:
            digits.insert(0, x % 10)
            x = x // 10
        return digits

    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.

        An integer is a palindrome when it reads the same forward and backward.
        """
        if x < 0:
            return False

        digits = self.digits(x)
        i, j = 0, len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True
