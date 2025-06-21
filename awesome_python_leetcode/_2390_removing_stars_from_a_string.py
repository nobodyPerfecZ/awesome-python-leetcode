class Solution:
    """Base class for all LeetCode Problems."""

    def removeStars(self, s: str) -> str:
        """
        You are given a string s, which contains stars *.

        In one operation, you can:
        - Choose a star in s.
        - Remove the closest non-star character to its left, as well as remove the star
        itself.

        Return the string after all stars have been removed.

        Note:
        - The input will be generated such that the operation is always possible.
        - It can be shown that the resulting string will always be unique.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = list(s)
        res = ""
        count = 0
        while stack:
            c = stack.pop()
            if c == "*":
                count += 1
            elif count == 0:
                res = c + res
            else:
                count -= 1
        return res
