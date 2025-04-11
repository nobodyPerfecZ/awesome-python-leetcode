import pytest

from awesome_python_leetcode._509_fibonacci_number import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, 1),
        (3, 2),
        (4, 3),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    fn = Solution().fib(n)
    assert fn == expected
