from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def countBits(self, n: int) -> List[int]:
        """
        Given an integer n, return an array ans of length n + 1 such that for each i
        (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
        """
        dp = [0 for _ in range(n + 1)]
        if n >= 1:
            dp[1] = 1
        for i in range(2, n + 1):
            offset = i & (1 << (i.bit_length() - 1)) - 1
            dp[i] = 1 + dp[offset]
        return dp
