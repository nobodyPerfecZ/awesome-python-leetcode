from typing import List

import pytest

from awesome_python_leetcode._289_game_of_life import Solution


@pytest.mark.parametrize(
    argnames=["board", "expected"],
    argvalues=[
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ],
)
def test_func(board: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    Solution().gameOfLife(board)
    assert board == expected
