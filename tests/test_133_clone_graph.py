from typing import List

import pytest

from awesome_python_leetcode._133_clone_graph import Solution, Node


@pytest.mark.parametrize(
    argnames=["edges", "expected"],
    argvalues=[
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
    ],
)
def test_func(edges: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    # TODO: Add tests
    graph = Node.build(edges)
    expected = Node.build(expected)
    graph = Solution().cloneGraph(graph)
    assert graph == expected
