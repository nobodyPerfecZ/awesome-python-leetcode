class Solution:
    """Base class for all LeetCode Problems."""

    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
        """

        def power(x: float, n: int):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 != 0:
                x_n = self.myPow(x, n // 2)
                return x * x_n * x_n
            else:
                x_n = self.myPow(x, n // 2)
                return x_n * x_n

        res = power(x, abs(n))
        return res if n >= 0 else 1 / res
