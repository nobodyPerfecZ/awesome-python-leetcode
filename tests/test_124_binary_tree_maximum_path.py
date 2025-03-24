from typing import List

import pytest

from awesome_python_leetcode._124_binary_tree_maximum_path_sum import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
    ],
)
def test_func(root: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    max_path_sum = Solution().maxPathSum(root)
    assert max_path_sum == expected
