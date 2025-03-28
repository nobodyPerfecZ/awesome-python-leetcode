from typing import List

import pytest

from awesome_python_leetcode._909_snakes_and_ladders import Solution


@pytest.mark.parametrize(
    argnames=["board", "expected"],
    argvalues=[
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        ),
        ([[-1, -1], [-1, 3]], 1),
    ],
)
def test_func(board: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_rolls = Solution().snakesAndLadders(board)
    assert num_rolls == expected
