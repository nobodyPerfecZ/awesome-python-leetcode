# flake8: noqa
import pytest

from awesome_python_leetcode._28_find_the_index_of_the_first_occurrence_in_a_string import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["haystack", "needle", "expected"],
    argvalues=[
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    ],
)
def test_func(haystack: str, needle: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    index = Solution().strStr(haystack, needle)
    assert index == expected
