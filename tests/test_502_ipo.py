from typing import List

import pytest

from awesome_python_leetcode._502_ipo import Solution


@pytest.mark.parametrize(
    argnames=["k", "w", "profits", "capital", "expected"],
    argvalues=[
        (2, 0, [1, 2, 3], [0, 1, 1], 4),
        (3, 0, [1, 2, 3], [0, 1, 2], 6),
    ],
)
def test_func(
    k: int,
    w: int,
    profits: List[int],
    capital: List[int],
    expected: List[int],
):
    """Tests the solution of a LeetCode problem."""
    maximized_capital = Solution().findMaximizedCapital(k, w, profits, capital)
    assert maximized_capital == expected
