# flake8: noqa

import pytest

from awesome_python_leetcode._1312_minimum_insertion_steps_to_make_a_string_palindrome import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    min_insertions = Solution().minInsertions(s)
    assert min_insertions == expected
