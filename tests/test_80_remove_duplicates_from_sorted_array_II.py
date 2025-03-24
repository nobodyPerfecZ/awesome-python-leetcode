from typing import List

import pytest

from awesome_python_leetcode._80_remove_duplicates_from_sorted_array_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]),
    ],
)
def test_func(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    length = Solution().removeDuplicates(nums)
    assert nums[:length] == expected
