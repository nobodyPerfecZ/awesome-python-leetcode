import pytest

from awesome_python_leetcode._1456_maximum_number_of_vowels_in_a_substring_of_given_length import (  # noqa: E501
    Solution,
)


@pytest.mark.parametrize(
    argnames=["s", "k", "expected"],
    argvalues=[
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
    ],
)
def test_func(s: str, k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    max_vowels = Solution().maxVowels(s, k)
    assert max_vowels == expected
