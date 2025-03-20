from typing import List
import pytest

from awesome_python_leetcode._137_single_number_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
    ],
)
def test_func(nums: List[int], expected: str):
    num = Solution().singleNumber(nums)
    assert num == expected
