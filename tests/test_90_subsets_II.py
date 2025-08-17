from typing import List

import pytest

from awesome_python_leetcode._90_subsets_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
        ([0], [[], [0]]),
    ],
)
def test_func(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    subsets = Solution().subsetsWithDup(nums)
    assert subsets == expected
