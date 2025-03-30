from typing import List

import pytest

from awesome_python_leetcode._274_h_index import Solution


@pytest.mark.parametrize(
    argnames=["citations", "expected"],
    argvalues=[
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
    ],
)
def test_func(citations: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    h_index = Solution().hIndex(citations)
    assert h_index == expected
