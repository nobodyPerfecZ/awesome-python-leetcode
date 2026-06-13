from typing import List, Optional

import pytest

from awesome_python_leetcode._103_binary_tree_zigzag_level_order_traversal import (
    Solution,
)
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_func(root: List[Optional[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    zig_zag_level_order = Solution().zigzagLevelOrder(root_node)
    assert zig_zag_level_order == expected
