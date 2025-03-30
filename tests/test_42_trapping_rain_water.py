from typing import List
import pytest

from awesome_python_leetcode._42_trapping_rain_water import Solution


@pytest.mark.parametrize(
    argnames=["height", "expected"],
    argvalues=[
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_func(height: List[int], expected: str):
    """Tests the solution of a LeetCode problem."""
    water = Solution().trap(height)
    assert water == expected
