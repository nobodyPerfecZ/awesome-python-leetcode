from typing import List, Optional

import pytest

from awesome_python_leetcode._226_invert_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_func(root: List[Optional[int]], expected: List[Optional[int]]):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    solution = TreeNode.build(expected)
    actual = Solution().invertTree(root_node)
    assert actual == solution
