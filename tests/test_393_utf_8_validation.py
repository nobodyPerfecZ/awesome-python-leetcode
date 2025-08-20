from typing import List

import pytest

from awesome_python_leetcode._393_utf_8_validation import Solution


@pytest.mark.parametrize(
    argnames=["data", "expected"],
    argvalues=[
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ([230, 136, 145], True),
        ([145], False),
    ],
)
def test_func(data: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    is_valid_utf_8 = Solution().validUtf8(data)
    assert is_valid_utf_8 is expected
