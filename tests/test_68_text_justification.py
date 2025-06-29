from typing import List

import pytest

from awesome_python_leetcode._68_text_justification import Solution


@pytest.mark.parametrize(
    argnames=["words", "maxWidth", "expected"],
    argvalues=[
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            ["This    is    an", "example  of text", "justification.  "],
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            ["What   must   be", "acknowledgment  ", "shall be        "],
        ),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
        ),
    ],
)
def test_func(words: List[str], maxWidth: int, expected: List[List[str]]):
    """Tests the solution of a LeetCode problem."""
    justified_text = Solution().fullJustify(words, maxWidth)
    assert justified_text == expected
