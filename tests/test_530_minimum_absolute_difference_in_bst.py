from typing import List

import pytest

from awesome_python_leetcode._530_minimum_absolute_difference_in_bst import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[([4, 2, 6, 1, 3], 1), ([1, 0, 48, None, None, 12, 49], 1)],
)
def test_func(root: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    minimum_difference = Solution().getMinimumDifference(root)
    assert minimum_difference == expected
