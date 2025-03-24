from typing import List

import pytest

from awesome_python_leetcode._57_insert_interval import Solution


@pytest.mark.parametrize(
    argnames=["intervals", "newInterval", "expected"],
    argvalues=[
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
def test_func(
    intervals: List[List[int]],
    newInterval: List[int],
    expected: List[List[int]],
):
    """Tests the solution of a LeetCode problem."""
    inserted_intervals = Solution().insert(intervals, newInterval)
    assert inserted_intervals == expected
