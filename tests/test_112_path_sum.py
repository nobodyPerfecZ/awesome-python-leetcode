from typing import List

import pytest

from awesome_python_leetcode._112_path_sum import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "targetSum", "expected"],
    argvalues=[
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
    ],
)
def test_func(root: List[int], targetSum: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    root = TreeNode.build(root)
    has_path_sum = Solution().hasPathSum(root, targetSum)
    assert has_path_sum is expected
