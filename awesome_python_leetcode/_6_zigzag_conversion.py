class Solution:
    """Base class for all LeetCode Problems."""

    def convert(self, s: str, numRows: int) -> str:
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
        rows like this: (you may want to display this pattern in a fixed font for
        better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number
        of rows.
        """
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]
        i, depth, inc = 0, 0, True
        for i in range(len(s)):
            # Append char to current depth
            zigzag[depth].append(s[i])

            # Update inc/dec switch
            if depth == numRows - 1:
                inc = False
            elif depth == 0:
                inc = True

            # Update depth
            if inc:
                depth += 1
            else:
                depth -= 1
        return "".join(c for zig in zigzag for c in zig)
