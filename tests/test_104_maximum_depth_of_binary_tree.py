from typing import List

import pytest

from awesome_python_leetcode._104_maximum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ],
)
def test_func(root: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    max_depth = Solution().maxDepth(root)
    assert max_depth == expected
