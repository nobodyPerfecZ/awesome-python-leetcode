from typing import List

import pytest

from awesome_python_leetcode._162_find_peak_element import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    peak_idx = Solution().findPeakElement(nums)
    assert peak_idx == expected
