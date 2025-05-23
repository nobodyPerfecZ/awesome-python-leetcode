class Solution:
    """Base class for all LeetCode Problems."""

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
        s1 and s2.

        An interleaving of two strings s and t is a configuration where s and t are
        divided into n and m substrings respectively, such that:
        - s = s1 + s2 + ... + sn
        - t = t1 + t2 + ... + tm
        - |n - m| <= 1
        - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
        t3 + s3 + ...

        Note: a + b is the concatenation of strings a and b.
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[-1][-1] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and (s3[i + j] == s1[i]) and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and (s3[i + j] == s2[j]) and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
