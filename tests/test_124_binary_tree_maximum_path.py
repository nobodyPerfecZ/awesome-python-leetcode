from typing import List, Optional

import pytest

from awesome_python_leetcode._124_binary_tree_maximum_path_sum import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[([1, 2, 3], 6), ([-10, 9, 20, None, None, 15, 7], 42)],
)
def test_func(root: List[Optional[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    max_path_sum = Solution().maxPathSum(root_node)
    assert max_path_sum == expected
