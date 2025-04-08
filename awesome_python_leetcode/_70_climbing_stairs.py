class Solution:
    """Base class for all LeetCode Problems."""

    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you
        climb to the top?
        """
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
