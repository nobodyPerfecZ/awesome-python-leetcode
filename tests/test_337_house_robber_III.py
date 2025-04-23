from typing import List

import pytest

from awesome_python_leetcode._337_house_robber_III import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
    ],
)
def test_func(root: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    max_amount = Solution().rob(root)
    assert max_amount == expected
