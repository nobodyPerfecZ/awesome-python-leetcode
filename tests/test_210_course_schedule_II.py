from typing import List

import pytest

from awesome_python_leetcode._210_course_schedule_II import Solution


@pytest.mark.parametrize(
    argnames=["numCourses", "prerequisites", "expected"],
    argvalues=[
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),
        (1, [], [0]),
    ],
)
def test_func(numCourses: int, prerequisites: List[List[int]], expected: bool):
    """Tests the solution of a LeetCode problem."""
    order = Solution().findOrder(numCourses, prerequisites)
    assert order == expected
