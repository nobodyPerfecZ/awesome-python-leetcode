class Solution:
    """Base class for all LeetCode Problems."""

    def numDecodings(self, s: str) -> int:
        """
        You have intercepted a secret message encoded as a string of numbers. The
        message is decoded via the following mapping:
        - "1" -> 'A'
        -  "2" -> 'B'
        ...
        - "25" -> 'Y'
        - "26" -> 'Z'

        However, while decoding the message, you realize that there are many different
        ways you can decode the message because some codes are contained in other
        codes ("2" and "5" vs "25").

        For example, "11106" can be decoded into:
        - "AAJF" with the grouping (1, 1, 10, 6)
        - "KJF" with the grouping (11, 10, 6)
        - The grouping (1, 11, 06) is invalid because "06" is not a valid code
        (only "6" is valid).

        Note: there may be strings that are impossible to decode.

        Given a string s containing only digits, return the number of ways to decode it.
        If the entire string cannot be decoded in any valid way, return 0.

        The test cases are generated so that the answer fits in a 32-bit integer.
        """
        dp = [0 for _ in range(len(s) + 1)]
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
