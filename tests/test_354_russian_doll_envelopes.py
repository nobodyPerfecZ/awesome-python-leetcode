from typing import List

import pytest

from awesome_python_leetcode._354_russian_doll_envelopes import Solution


@pytest.mark.parametrize(
    argnames=["envelopes", "expected"],
    argvalues=[
        ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
        ([[1, 1], [1, 1], [1, 1]], 1),
        ([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]], 4),
    ],
)
def test_func_bs(envelopes: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_envelopes = Solution().maxEnvelopesBS(envelopes)
    assert max_envelopes == expected


@pytest.mark.parametrize(
    argnames=["envelopes", "expected"],
    argvalues=[
        ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
        ([[1, 1], [1, 1], [1, 1]], 1),
        ([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]], 4),
    ],
)
def test_func_dp(envelopes: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_envelopes = Solution().maxEnvelopesDP(envelopes)
    assert max_envelopes == expected
