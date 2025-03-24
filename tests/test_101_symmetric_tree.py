from typing import List

import pytest

from awesome_python_leetcode._101_symmetric_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
    ],
)
def test_func(root: List[int], expected: bool):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    is_symmetric = Solution().isSymmetric(root)
    assert is_symmetric == expected
