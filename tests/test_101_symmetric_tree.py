from typing import List, Optional

import pytest

from awesome_python_leetcode._101_symmetric_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[([1, 2, 2, 3, 4, 4, 3], True), ([1, 2, 2, None, 3, None, 3], False)],
)
def test_func(root: List[Optional[int]], expected: bool):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    is_symmetric = Solution().isSymmetric(root_node)
    assert is_symmetric is expected
