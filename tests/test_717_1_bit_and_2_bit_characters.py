from typing import List

import pytest

from awesome_python_leetcode._717_1_bit_and_2_bit_characters import Solution


@pytest.mark.parametrize(
    argnames=["bits", "expected"],
    argvalues=[
        ([1, 0, 0], True),
        ([1, 1, 1, 0], False),
    ],
)
def test_func(bits: List[int], expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_one_bit_character = Solution().isOneBitCharacter(bits)
    assert is_one_bit_character is expected
