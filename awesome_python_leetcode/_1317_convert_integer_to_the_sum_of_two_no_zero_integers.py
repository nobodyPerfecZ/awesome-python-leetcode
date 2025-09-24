from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def hasZeros(self, n: int) -> bool:
        """Check if the integer n has any zeros in its decimal representation."""
        while n != 0:
            digit = n % 10
            if digit == 0:
                return True
            n = n // 10
        return False

    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        No-Zero integer is a positive integer that does not contain any 0 in its decimal
        representation.

        Given an integer n, return a list of two integers [a, b] where:
        - a and b are No-Zero integers.
        - a + b = n

        The test cases are generated so that there is at least one valid solution. If
        there are many valid solutions, you can return any of them.
        """
        num1 = n // 2 + 1 if n % 2 else n // 2
        num2 = n // 2
        while self.hasZeros(num1) or self.hasZeros(num2):
            num1 -= 1
            num2 += 1
        return [num1, num2]
