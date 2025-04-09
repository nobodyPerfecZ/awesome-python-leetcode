from typing import List

import pytest

from awesome_python_leetcode._63_unique_paths_II import Solution


@pytest.mark.parametrize(
    argnames=["obstacleGrid", "expected"],
    argvalues=[
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[1]], 0),
    ],
)
def test_func(obstacleGrid: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_paths = Solution().uniquePathsWithObstacles(obstacleGrid)
    assert num_paths == expected
