class Solution:
    """Base class for all LeetCode Problems."""

    def countCommas(self, n: int) -> int:
        """
        You are given an integer n.

        Return the total number of commas used when writing all integers from [1, n]
        (inclusive) in standard number formatting.

        In standard formatting:
        - A comma is inserted after every three digits from the right.
        - Numbers with fewer than 4 digits contain no commas.
        """
        return max(0, n - 1000 + 1)
