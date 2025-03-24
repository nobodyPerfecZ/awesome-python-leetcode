# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._117_populating_next_right_pointers_in_each_node_II import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5, None, 7], [1, None, 2, 3, None, 4, 5, 7, None]),
        ([], []),
    ],
)
def test_func(root: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    connected_root = Solution().connect(root)
    print(root)
    assert TreeNode.compare_next(connected_root, expected) is True
