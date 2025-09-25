import pytest

from awesome_python_leetcode._1935_maximum_number_of_words_you_can_type import Solution


@pytest.mark.parametrize(
    argnames=["text", "brokenLetters", "expected"],
    argvalues=[
        ("hello world", "ad", 1),
        ("leet code", "lt", 1),
        ("leet code", "e", 0),
    ],
)
def test_func(text: str, brokenLetters: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_typed_words = Solution().canBeTypedWords(text, brokenLetters)
    assert num_typed_words == expected
