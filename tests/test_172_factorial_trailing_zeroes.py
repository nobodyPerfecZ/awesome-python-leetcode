import pytest

from awesome_python_leetcode._172_factorial_trailing_zeros import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (3, 0),
        (5, 1),
        (0, 0),
        (7, 1),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    trailing_zeroes = Solution().trailingZeroes(n)
    assert trailing_zeroes == expected
