import pytest

from awesome_python_leetcode._29_divide_two_integers import Solution


@pytest.mark.parametrize(
    argnames=["dividend", "divisor", "expected"],
    argvalues=[
        (10, 3, 3),
        (7, -3, -2),
        (-2147483648, -1, 2147483647),
    ],
)
def test_func(dividend: int, divisor: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    result = Solution().divide(dividend, divisor)
    assert result == expected
