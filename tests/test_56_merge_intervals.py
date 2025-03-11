from typing import List

import pytest

from awesome_python_leetcode._56_merge_intervals import Solution


@pytest.mark.parametrize(
    argnames=["intervals", "expected"],
    argvalues=[
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ],
)
def test_func(intervals: List[List[int]], expected: List[List[int]]):
    merged_intervals = Solution().merge(intervals)
    assert merged_intervals == expected
