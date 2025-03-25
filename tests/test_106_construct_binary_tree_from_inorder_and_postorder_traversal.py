# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._106_construct_binary_tree_from_inorder_and_postorder_traversal import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["inorder", "postorder", "expected"],
    argvalues=[
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ],
)
def test_func(inorder: List[int], postorder: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    solution = TreeNode.build(expected)
    actual = Solution().buildTree(inorder, postorder)
    assert actual == solution
