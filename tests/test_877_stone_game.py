from typing import List

import pytest

from awesome_python_leetcode._877_stone_game import Solution


@pytest.mark.parametrize(
    argnames=["piles", "expected"],
    argvalues=[
        ([5, 3, 4, 5], True),
        ([3, 7, 2, 3], True),
    ],
)
def test_func(piles: List[int], expected: bool):
    """Tests the solution of a LeetCode problem."""
    alice_won = Solution().stoneGame(piles)
    assert alice_won == expected
