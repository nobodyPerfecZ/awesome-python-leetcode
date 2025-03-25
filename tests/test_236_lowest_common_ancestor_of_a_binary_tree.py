from typing import List

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
def test_func(root: List[int], p: int, q: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    p = TreeNode.find(root, p)
    q = TreeNode.find(root, q)
    solution = TreeNode.find(root, expected)
    lowest_common_ancestor = Solution().lowestCommonAncestor(root, p, q)
    assert lowest_common_ancestor == solution
