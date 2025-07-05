from typing import List

import pytest

from awesome_python_leetcode._594_longest_harmonious_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 3, 2, 2, 5, 2, 3, 7], 5),
        ([1, 2, 3, 4], 2),
        ([1, 1, 1, 1], 0),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    lhs = Solution().findLHS(nums)
    assert lhs == expected
