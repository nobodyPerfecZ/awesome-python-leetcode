from typing import List

import pytest

from awesome_python_leetcode._100_same_tree import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["p", "q", "expected"],
    argvalues=[
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_func(p: List[int], q: List[int], expected: bool):
    """Tests the solution of a LeetCode problem."""
    p = TreeNode.build(p)
    q = TreeNode.build(q)
    is_same_tree = Solution().isSameTree(p, q)
    assert is_same_tree == expected
