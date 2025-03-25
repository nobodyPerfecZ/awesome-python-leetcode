from typing import List

import pytest

from awesome_python_leetcode._114_flatten_binary_tree_to_linked_list import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([], []),
        ([0], [0]),
    ],
)
def test_func(root: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    solution = TreeNode.build(expected)
    Solution().flatten(root)
    assert root == solution
