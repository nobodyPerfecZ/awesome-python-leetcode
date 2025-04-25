from typing import List

import pytest

from awesome_python_leetcode._646_maximum_length_of_pair_chain import Solution


@pytest.mark.parametrize(
    argnames=["pairs", "expected"],
    argvalues=[
        ([[1, 2], [2, 3], [3, 4]], 2),
        ([[1, 2], [7, 8], [4, 5]], 3),
    ],
)
def test_func(pairs: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    longest_chain = Solution().findLongestChain(pairs)
    assert longest_chain == expected
