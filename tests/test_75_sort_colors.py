from typing import List

import pytest

from awesome_python_leetcode._75_sort_colors import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
    ],
)
def test_func_bs(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    Solution().sortColorsBS(nums)
    assert nums == expected


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
    ],
)
def test_func_qs(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    Solution().sortColorsQS(nums)
    assert nums == expected
