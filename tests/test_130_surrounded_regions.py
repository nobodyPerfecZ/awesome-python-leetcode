from typing import List

import pytest

from awesome_python_leetcode._130_surrounded_regions import Solution


@pytest.mark.parametrize(
    argnames=["grid", "expected"],
    argvalues=[
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        ([["X"]], [["X"]]),
        (
            [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
            [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
        ),
    ],
)
def test_func(grid: List[List[str]], expected: List[List[str]]):
    """Tests the solution of a LeetCode problem."""
    Solution().solve(grid)
    assert grid == expected
