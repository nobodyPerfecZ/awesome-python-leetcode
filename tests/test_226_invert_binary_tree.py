from typing import List

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
def test_func(root: List[int], expected: List[int]):
    root = TreeNode.build(root)
    solution = TreeNode.build(expected)
    actual = Solution().invertTree(root)
    assert TreeNode.compare(actual, solution) is True
