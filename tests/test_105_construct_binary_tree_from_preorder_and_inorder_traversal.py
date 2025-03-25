# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._105_construct_binary_tree_from_preorder_and_inorder_traversal import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["preorder", "inorder", "expected"],
    argvalues=[
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ],
)
def test_func(preorder: List[int], inorder: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    solution = TreeNode.build(expected)
    actual = Solution().buildTree(preorder, inorder)
    assert actual == solution
