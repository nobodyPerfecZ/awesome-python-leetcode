class Solution:
    """Base class for all LeetCode Problems."""

    def isMatchTD(self, s: str, p: str) -> bool:
        """
        Given an input string s and a pattern p, implement regular expression matching
        with support for '.' and '*' where:
        - '.' Matches any single characters.
        - '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).
        """
        # Top-Down Dynamic Programming (Memoization)
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

    def isMatchBU(self, s: str, p: str) -> bool:
        """
        Given an input string s and a pattern p, implement regular expression matching
        with support for '.' and '*' where:
        - '.' Matches any single characters.
        - '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).
        """
        # Bottom-Up Dynamic Programming (Tabulation)
        # Time Complexity: O(n²)
        # Space Complexity: O(n²)
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        # Initialize first row
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]
