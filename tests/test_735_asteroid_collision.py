from typing import List

import pytest

from awesome_python_leetcode._735_asteroid_collision import Solution


@pytest.mark.parametrize(
    argnames=["asteroids", "expected"],
    argvalues=[
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
    ],
)
def test_func(asteroids: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    asteroids_left = Solution().asteroidCollision(asteroids)
    assert asteroids_left == expected
