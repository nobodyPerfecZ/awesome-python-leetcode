from typing import List

import pytest

from awesome_python_leetcode._477_total_hamming_distance import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([4, 14, 2], 6),
        ([4, 14, 4], 4),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    total_hamming_distance = Solution().totalHammingDistance(nums)
    assert total_hamming_distance == expected
