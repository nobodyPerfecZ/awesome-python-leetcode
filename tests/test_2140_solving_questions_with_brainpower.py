from typing import List

import pytest

from awesome_python_leetcode._2140_solving_questions_with_brainpower import Solution


@pytest.mark.parametrize(
    argnames=["questions", "expected"],
    argvalues=[
        ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
    ],
)
def test_func(questions: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_points = Solution().mostPoints(questions)
    assert max_points == expected
