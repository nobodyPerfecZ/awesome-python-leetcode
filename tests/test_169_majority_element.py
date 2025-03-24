from typing import List

import pytest

from awesome_python_leetcode._169_majority_element import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    majority_element = Solution().majorityElement(nums)
    assert majority_element == expected
