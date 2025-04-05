from typing import List

import pytest

from awesome_python_leetcode._51_n_queens import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
        (1, [["Q"]]),
    ],
)
def test_func(n: int, expected: List[List[str]]):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().solveNQueens(n)
    assert combinations == expected
