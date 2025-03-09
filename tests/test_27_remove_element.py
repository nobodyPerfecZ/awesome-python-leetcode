from typing import List

import pytest

from awesome_python_leetcode._27_remove_element import Solution


@pytest.mark.parametrize(
    argnames=["nums", "val", "expected"],
    argvalues=[
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
    ],
)
def test_func(nums: List[int], val: int, expected: List[int]):
    length = Solution().removeElement(nums, val)
    assert nums[:length] == expected
