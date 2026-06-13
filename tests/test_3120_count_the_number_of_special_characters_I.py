import pytest

from awesome_python_leetcode._3120_count_the_number_of_special_characters_I import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["word", "expected"],
    argvalues=[
        ("aaAbcBC", 3),
        ("abc", 0),
        ("abBCab", 1),
    ],
)
def test_func(word: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_special_char = Solution().numberOfSpecialChars(word)
    assert num_special_char == expected
