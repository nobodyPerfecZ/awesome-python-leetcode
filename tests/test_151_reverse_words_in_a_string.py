import pytest

from awesome_python_leetcode._151_reverse_words_in_a_string import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
def test_func(s: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    reverse = Solution().reverseWords(s)
    assert reverse == expected
