from typing import List

import pytest

from awesome_python_leetcode._1991_find_the_middle_index_in_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 3, -1, 8, 4], 3),
        ([1, -1, 4], 2),
        ([2, 5], -1),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    middle_idx = Solution().findMiddleIndex(nums)
    assert middle_idx == expected
