class Solution:
    """Base class for all LeetCode Problems."""

    def decodeString(self, s: str) -> str:
        """
        Given an encoded string, return its decoded string.

        The encoding rule is: k[encoded_string], where the encoded_string inside the
        square brackets is being repeated exactly k times. Note that k is guaranteed to
        be a positive integer.

        You may assume that the input string is always valid; there are no extra white
        spaces, square brackets are well-formed, etc. Furthermore, you may assume that
        the original data does not contain any digits and that digits are only for those
        repeat numbers, k. For example, there will not be input like 3a or 2[4].

        The test cases are generated so that the length of the output will never exceed
        10^5.
        """
        decode = ""
        i = 0
        while i < len(s):
            # Check if character is a string
            if s[i] >= "a" and s[i] <= "z":
                decode += s[i]
                i += 1
                continue
            # Get the occurence for the open bracket [
            j = i
            while j < len(s) and s[j] != "[":
                j += 1
            number = int(str(s[i:j]))

            # Get the last occurence for the closed bracket ]
            openBrackets = 1
            k = j + 1
            while k < len(s) and openBrackets > 0:
                if s[k] == "[":
                    openBrackets += 1
                if s[k] == "]":
                    openBrackets -= 1
                k += 1
            substr = self.decodeString(s[j + 1 : k - 1])
            decode += number * substr
            i = k
        return decode
