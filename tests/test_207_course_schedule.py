from typing import List

import pytest

from awesome_python_leetcode._207_course_schedule import Solution


@pytest.mark.parametrize(
    argnames=["numCourses", "prerequisites", "expected"],
    argvalues=[
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
    ],
)
def test_func(numCourses: int, prerequisites: List[List[int]], expected: bool):
    """Tests the solution of a LeetCode problem."""
    can_finish = Solution().canFinish(numCourses, prerequisites)
    assert can_finish is expected
