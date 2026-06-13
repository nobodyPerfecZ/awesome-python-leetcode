from typing import List, Optional

import pytest

from awesome_python_leetcode._98_validate_binary_search_tree import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([32, 26, 47, 19, None, None, 56, None, 27], False),
    ],
)
def test_func(root: List[Optional[int]], expected: bool):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    is_valid_bst = Solution().isValidBST(root_node)
    assert is_valid_bst is expected
