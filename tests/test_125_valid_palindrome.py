import pytest

from awesome_python_leetcode._125_valid_palindrome import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_func(s: str, expected: bool):
    max_profit = Solution().isPalindrome(s)
    assert max_profit == expected
