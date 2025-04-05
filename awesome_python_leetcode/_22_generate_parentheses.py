from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of
        well-formed parentheses.
        """
        res = []

        def dfs(p: str, openP: int, endP: int):
            if openP == n and endP == n:
                res.append(p)
                return
            if openP < n:
                dfs(p + "(", openP + 1, endP)
            if openP > endP and endP < n:
                dfs(p + ")", openP, endP + 1)

        dfs("", 0, 0)
        return res
