from typing import List

import pytest

from awesome_python_leetcode._1140_stone_game_II import Solution


@pytest.mark.parametrize(
    argnames=["piles", "expected"],
    argvalues=[
        ([2, 7, 9, 4, 4], 10),
        ([1, 2, 3, 4, 5, 100], 104),
    ],
)
def test_func(piles: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_stones = Solution().stoneGameII(piles)
    assert num_stones == expected
