# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._1964_find_the_longest_valid_obstacle_course_at_each_position import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["obstacles", "expected"],
    argvalues=[
        ([1, 2, 3, 2], [1, 2, 3, 3]),
        ([2, 2, 1], [1, 2, 1]),
        ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
    ],
)
def test_func(obstacles: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    longest_obstacles = Solution().longestObstacleCourseAtEachPosition(obstacles)
    assert longest_obstacles == expected
