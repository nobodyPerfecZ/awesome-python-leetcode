import pytest

from awesome_python_leetcode._58_length_of_last_word import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    length = Solution().lengthOfLastWord(s)
    assert length == expected
