import pytest

from awesome_python_leetcode._279_perfect_squares import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (12, 3),
        (13, 2),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_squares = Solution().numSquares(n)
    assert num_squares == expected
