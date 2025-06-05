import pytest

from awesome_python_leetcode._415_add_strings import Solution


@pytest.mark.parametrize(
    argnames=["num1", "num2", "expected"],
    argvalues=[
        ("11", "123", "134"),
        ("456", "77", "533"),
        ("0", "0", "0"),
        ("9", "99", "108"),
    ],
)
def test_func(num1: str, num2: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    num3 = Solution().addStrings(num1, num2)
    assert num3 == expected
