from typing import List

import pytest

from awesome_python_leetcode._2154_keep_multiplying_found_values_by_two import Solution


@pytest.mark.parametrize(
    argnames=["nums", "original", "expected"],
    argvalues=[
        ([5, 3, 6, 1, 12], 3, 24),
        ([2, 7, 9], 4, 4),
    ],
)
def test_func(nums: List[int], original: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    final_value = Solution().findFinalValue(nums, original)
    assert final_value == expected
