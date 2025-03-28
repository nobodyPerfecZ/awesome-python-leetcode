from typing import List

import pytest

from awesome_python_leetcode._399_evaluate_division import Solution


@pytest.mark.parametrize(
    argnames=["equations", "values", "queries", "expected"],
    argvalues=[
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000],
        ),
        (
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.50000, 2.00000, -1.00000, -1.00000],
        ),
    ],
)
def test_func(
    equations: List[List[str]],
    values: List[float],
    queries: List[List[str]],
    expected: List[float],
):
    """Tests the solution of a LeetCode problem."""
    solutions = Solution().calcEquation(equations, values, queries)
    assert solutions == expected
