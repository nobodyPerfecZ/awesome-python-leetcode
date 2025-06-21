from typing import List

import pytest

from awesome_python_leetcode._1679_max_number_of_k_sum_pairs import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3, 4),
    ],
)
def test_func(nums: List[int], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    max_operations = Solution().maxOperations(nums, k)
    assert max_operations == expected
