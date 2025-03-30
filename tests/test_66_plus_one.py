from typing import List
import pytest

from awesome_python_leetcode._66_plus_one import Solution


@pytest.mark.parametrize(
    argnames=["digits", "expected"],
    argvalues=[
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ],
)
def test_func(digits: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    digits = Solution().plusOne(digits)
    assert digits == expected
