from typing import List

import pytest

from awesome_python_leetcode._3005_count_elements_with_maximum_frequency import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 2, 3, 1, 4], 4),
        ([1, 2, 3, 4, 5], 5),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_frequency = Solution().maxFrequencyElements(nums)
    assert max_frequency == expected
