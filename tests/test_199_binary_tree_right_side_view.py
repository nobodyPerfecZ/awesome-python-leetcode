from typing import List

import pytest

from awesome_python_leetcode._199_binary_tree_right_side_view import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ],
)
def test_func(root: List[int], expected: List[int]):
    root = TreeNode.build(root)
    right_side_view = Solution().rightSideView(root)
    assert right_side_view == expected
