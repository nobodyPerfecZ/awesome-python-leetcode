import pytest

from awesome_python_leetcode._2785_sort_vowels_in_a_string import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("lEetcOde", "lEOtcede"),
        ("lYmpH", "lYmpH"),
    ],
)
def test_func(s: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    sorted_s = Solution().sortVowels(s)
    assert sorted_s == expected
