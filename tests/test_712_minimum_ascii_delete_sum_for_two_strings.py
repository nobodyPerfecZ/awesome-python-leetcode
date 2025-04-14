import pytest

from awesome_python_leetcode._712_minimum_ascii_delete_sum_for_two_strings import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["s1", "s2", "expected"],
    argvalues=[
        ("sea", "eat", 231),
        ("delete", "leet", 403),
    ],
)
def test_func(s1: str, s2: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    delete_sum = Solution().minimumDeleteSum(s1, s2)
    assert delete_sum == expected
