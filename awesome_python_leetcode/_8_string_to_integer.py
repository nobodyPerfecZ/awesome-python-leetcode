class Solution:
    """Base class for all LeetCode Problems."""

    def myAtoi(self, s: str) -> int:
        """
        Implement the myAtoi(string s) function, which converts a string to a 32-bit
        signed integer.

        The algorithm for myAtoi(string s) is as follows:
        1. Whitespace: Ignore any leading whitespace (" ").
        2. Signedness: Determine the sign by checking if the next character is '-' or
        '+', assuming positivity if neither present.
        3. Conversion: Read the integer by skipping leading zeros until a non-digit
        character is encountered or the end of the string is reached. If no digits were
        read, then the result is 0.
        4. Rounding: If the integer is out of the 32-bit signed integer range
        [-231, 231 - 1], then round the integer to remain in the range. Specifically,
        integers less than -231 should be rounded to -231, and integers greater than
        231 - 1 should be rounded to 231 - 1.

        Return the integer as the final result.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        i = 0
        # Ignore any leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Out out bounds
        if i >= len(s) or s[i] not in ["-", "+"] and s[i] <= "0" and s[i] >= "9":
            return 0

        # Check for signs
        sign = "+"
        if s[i] in ["-", "+"]:
            sign = s[i]
            i += 1

        # Iterate through number until non-digit
        j = i
        while j < len(s) and s[j] >= "0" and s[j] <= "9":
            j += 1

        # Out of bounds (only sign and no digits)
        if j == i:
            return 0

        # Return the parsed number
        num = int(s[i:j])

        # Clip to the range [-2**31, 2**31 - 1]
        if sign == "+" and num >= 2**31:
            return 2**31 - 1
        elif sign == "+" and num < 2**31:
            return num
        elif sign == "-" and num >= 2**31:
            return -(2**31)
        else:
            return -num
