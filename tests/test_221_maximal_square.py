from typing import List

import pytest

from awesome_python_leetcode._221_maximal_square import Solution


@pytest.mark.parametrize(
    argnames=["matrix", "expected"],
    argvalues=[
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        ([["0", "1"], ["1", "0"]], 1),
        ([["0"]], 0),
    ],
)
def test_func(matrix: List[List[str]], expected: int):
    """Tests the solution of a LeetCode problem."""
    square = Solution().maximalSquare(matrix)
    assert square == expected
