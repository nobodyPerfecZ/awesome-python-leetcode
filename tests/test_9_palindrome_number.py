import pytest

from awesome_python_leetcode._9_palindrome_number import Solution


@pytest.mark.parametrize(
    argnames=["x", "expected"],
    argvalues=[
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_func(x: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_palindrome = Solution().isPalindrome(x)
    assert is_palindrome is expected
