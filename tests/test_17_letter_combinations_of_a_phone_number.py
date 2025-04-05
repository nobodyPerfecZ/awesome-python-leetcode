from typing import List

import pytest

from awesome_python_leetcode._17_letter_combinations_of_a_phone_number import Solution


@pytest.mark.parametrize(
    argnames=["digits", "expected"],
    argvalues=[
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ],
)
def test_func(digits: str, expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    letters = Solution().letterCombinations(digits)
    assert letters == expected
