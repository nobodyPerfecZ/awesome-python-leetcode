import pytest

from awesome_python_leetcode._342_power_of_four import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (16, True),
        (5, False),
        (1, True),
    ],
)
def test_func(n: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_power_of_four = Solution().isPowerOfFour(n)
    assert is_power_of_four is expected
