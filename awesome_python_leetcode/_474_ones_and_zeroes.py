from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        You are given an array of binary strings strs and two integers m and n.

        Return the size of the largest subset of strs such that there are at most m 0's
        and n 1's in the subset.

        A set x is a subset of a set y if all elements of x are also elements of y.
        """
        dp = {}

        def dfs(i: int, m: int, n: int):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            zeroes = strs[i].count("0")
            ones = strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if zeroes <= m and ones <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - zeroes, n - ones),
                )
            return dp[(i, m, n)]

        return dfs(0, m, n)
