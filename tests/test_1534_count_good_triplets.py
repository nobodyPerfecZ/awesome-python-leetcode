from typing import List

import pytest

from awesome_python_leetcode._1534_count_good_triplets import Solution


@pytest.mark.parametrize(
    argnames=["arr", "a", "b", "c", "expected"],
    argvalues=[
        ([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
        ([1, 1, 2, 2, 3], 0, 0, 1, 0),
    ],
)
def test_func(arr: List[int], a: int, b: int, c: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_good_triplets = Solution().countGoodTriplets(arr, a, b, c)
    assert num_good_triplets == expected
