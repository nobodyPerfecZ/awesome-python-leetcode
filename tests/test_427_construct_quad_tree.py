from typing import List

import pytest

from awesome_python_leetcode._427_construct_quad_tree import QuadTreeNode, Solution


@pytest.mark.parametrize(
    argnames=["grid", "expected"],
    argvalues=[
        ([[0, 1], [1, 0]], [[0, 0], [1, 0], [1, 1], [1, 1], [1, 0]]),
        (
            [
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
            ],
            [
                [0, 0],
                [1, 1],
                [0, 0],
                [1, 1],
                [1, 0],
                None,
                None,
                None,
                None,
                [1, 0],
                [1, 0],
                [1, 1],
                [1, 1],
            ],
        ),
    ],
)
def test_func(grid: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    actual = Solution().construct(grid)
    expected = QuadTreeNode.build(expected)
    assert actual == expected
