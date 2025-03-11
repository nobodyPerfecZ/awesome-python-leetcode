from typing import List

import pytest

from awesome_python_leetcode._452_minimum_number_of_arrows_to_burst_balloons import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["points", "expected"],
    argvalues=[
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ],
)
def test_func(points: List[List[int]], expected: int):
    min_arrow_shots = Solution().findMinArrowShots(points)
    assert min_arrow_shots == expected
