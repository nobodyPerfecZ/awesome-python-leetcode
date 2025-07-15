import pytest

from awesome_python_leetcode._3136_valid_word import Solution


@pytest.mark.parametrize(
    argnames=["word", "expected"],
    argvalues=[
        ("234Adas", True),
        ("b3", False),
        ("a3$e", False),
    ],
)
def test_func(word: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_valid = Solution().isValid(word)
    assert is_valid is expected
