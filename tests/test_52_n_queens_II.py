import pytest

from awesome_python_leetcode._52_n_queens_II import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (4, 2),
        (1, 1),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().totalNQueens(n)
    assert combinations == expected
