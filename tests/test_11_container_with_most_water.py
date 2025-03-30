from typing import List

import pytest

from awesome_python_leetcode._11_container_with_most_water import Solution


@pytest.mark.parametrize(
    argnames=["height", "expected"],
    argvalues=[
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_func(height: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_area = Solution().maxArea(height)
    assert max_area == expected
