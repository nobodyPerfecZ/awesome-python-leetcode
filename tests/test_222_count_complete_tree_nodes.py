from typing import List, Optional

import pytest

from awesome_python_leetcode._222_count_complete_tree_nodes import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[([1, 2, 3, 4, 5, 6], 6), ([], 0), ([1], 1)],
)
def test_func(root: List[Optional[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    num_nodes = Solution().countNodes(root_node)
    assert num_nodes == expected
