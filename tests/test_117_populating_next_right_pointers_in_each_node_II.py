from typing import List, Optional

import pytest

import awesome_python_leetcode._117_populating_next_right_pointers_in_each_node_II as prob  # noqa: E501


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5, None, 7], [1, None, 2, 3, None, 4, 5, 7, None]),
        ([], []),
    ],
)
def test_func(root: List[Optional[int]], expected: List[Optional[int]]):
    """Tests the solution of a LeetCode problem."""
    root_node = prob.TreeNode.build(root)
    expected_val: Optional[List[Optional[int]]] = expected if expected else None
    if root_node is not None:
        connected_root = prob.Solution().connect(root_node)
        assert connected_root == expected_val
    else:
        assert root_node == expected_val
