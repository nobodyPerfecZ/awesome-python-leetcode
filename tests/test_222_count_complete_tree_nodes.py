from typing import List

import pytest

from awesome_python_leetcode._222_count_complete_tree_nodes import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5, 6], 6),
        ([], 0),
        ([1], 1),
    ],
)
def test_func(root: List[int], expected: int):
    root = TreeNode.build(root)
    num_nodes = Solution().countNodes(root)
    assert num_nodes == expected
