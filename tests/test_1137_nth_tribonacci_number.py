import pytest

from awesome_python_leetcode._1137_nth_tribonacci_number import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (4, 4),
        (25, 1389537),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    tn = Solution().tribonacci(n)
    assert tn == expected
