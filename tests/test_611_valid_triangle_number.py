from typing import List

import pytest

from awesome_python_leetcode._611_valid_triangle_number import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 2, 3, 4], 3),
        ([4, 2, 3, 4], 4),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_triangles = Solution().triangleNumber(nums)
    assert num_triangles == expected
