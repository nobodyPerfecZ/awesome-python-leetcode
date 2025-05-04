from typing import List

import pytest

from awesome_python_leetcode._1732_find_the_highest_altitude import Solution


@pytest.mark.parametrize(
    argnames=["gain", "expected"],
    argvalues=[
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ],
)
def test_func(gain: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    largest_altitude = Solution().largestAltitude(gain)
    assert largest_altitude == expected
