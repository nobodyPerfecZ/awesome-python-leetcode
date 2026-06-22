class Solution:
    """Base class for all LeetCode Problems."""

    def addDigits(self, num: int) -> int:
        """
        Given an integer num, repeatedly add all its digits until the result has
        only one digit, and return it.
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
