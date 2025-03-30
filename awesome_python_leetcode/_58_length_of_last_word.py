class Solution:
    """Base class for all LeetCode Problems."""

    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of words and spaces, return the length of the last
        word in the string.

        A word is a maximal substring consisting of non-space characters only.
        """
        return len(s.split()[-1])
