from typing import List
import pytest

from awesome_python_leetcode._136_single_number import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_func(nums: List[int], expected: int):
    num = Solution().singleNumber(nums)
    assert num == expected
