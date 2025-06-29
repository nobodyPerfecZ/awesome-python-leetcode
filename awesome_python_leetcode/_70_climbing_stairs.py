class Solution:
    """Base class for all LeetCode Problems."""

    def climbStairsTD(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you
        climb to the top?
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        dp = {}

        def dfs(m: int) -> int:
            if m == 0:
                return 1
            elif m == 1:
                return 1
            elif m in dp:
                return dp[m]
            else:
                dp[m - 1] = dfs(m - 1)
                dp[m - 2] = dfs(m - 2)
                dp[m] = dp[m - 1] + dp[m - 2]
                return dp[m]

        return dfs(n)

    def climbStairsBU(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you
        climb to the top?
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climbStairsBUOptimized(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you
        climb to the top?
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        one, two = 1, 1
        for _ in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
