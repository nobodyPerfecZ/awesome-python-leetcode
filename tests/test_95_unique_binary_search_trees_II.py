from typing import List

import pytest

from awesome_python_leetcode._95_unique_binary_search_trees_II import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (
            3,
            [
                [1, None, 2, None, 3],
                [1, None, 3, 2],
                [2, 1, 3],
                [3, 1, None, None, 2],
                [3, 2, None, 1],
            ],
        ),
        (1, [[1]]),
    ],
)
def test_func(n: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    expected = [TreeNode.build(tree) for tree in expected]
    bsts = Solution().generateTrees(n)
    assert all(actual == expected for actual, expected in zip(bsts, expected))
