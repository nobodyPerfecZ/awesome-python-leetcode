from typing import List

import pytest

from awesome_python_leetcode._219_contains_duplicate_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ],
)
def test_func(nums: List[int], k: int, expected: bool):
    contains_nearby_duplicate = Solution().containsNearbyDuplicate(nums, k)
    assert contains_nearby_duplicate == expected
