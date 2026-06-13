from typing import List, Optional

import pytest

from awesome_python_leetcode._236_lowest_common_ancestor_of_a_binary_tree import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["root", "p", "q", "expected"],
    argvalues=[
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
    ],
)
def test_func(root: List[Optional[int]], p: int, q: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    p_node = TreeNode.find(root_node, p)
    q_node = TreeNode.find(root_node, q)
    expected_node = TreeNode.find(root_node, expected)

    if root_node is not None and p_node is not None and q_node is not None:
        lowest_common_ancestor = Solution().lowestCommonAncestor(
            root_node, p_node, q_node
        )
        assert lowest_common_ancestor == expected_node
