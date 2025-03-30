from typing import List

import pytest

from awesome_python_leetcode._238_product_of_array_except_self import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])],
)
def test_func(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    products = Solution().productExceptSelf(nums)
    assert products == expected
