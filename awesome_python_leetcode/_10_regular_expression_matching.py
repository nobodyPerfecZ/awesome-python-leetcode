class Solution:
    """Base class for all LeetCode Problems."""

    def isMatch(self, s: str, p: str) -> bool:
        """
        Given an input string s and a pattern p, implement regular expression matching
        with support for '.' and '*' where:
        - '.' Matches any single characters.
        - '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).
        """
        # Time Complexity: O(n²)
        # Space Complexity: O(n²)
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
