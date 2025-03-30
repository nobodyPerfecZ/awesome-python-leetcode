import numpy as np
import pytest

from awesome_python_leetcode._50_pow_x_n import Solution


@pytest.mark.parametrize(
    argnames=["x", "n", "expected"],
    argvalues=[
        (2.00000, 10, 1024.00000),
        (2.10000, 3, 9.26100),
        (2.00000, -2, 0.25000),
    ],
)
def test_func(x: int, n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    power = Solution().myPow(x, n)
    np.testing.assert_allclose(power, expected)
