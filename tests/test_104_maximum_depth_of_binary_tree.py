from typing import List, Optional

import pytest

from awesome_python_leetcode._104_maximum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[([3, 9, 20, None, None, 15, 7], 3), ([1, None, 2], 2)],
)
def test_func(root: List[Optional[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    max_depth = Solution().maxDepth(root_node)
    assert max_depth == expected
