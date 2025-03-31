from typing import List

import pytest

from awesome_python_leetcode._30_substring_with_concatenation_of_all_words import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["s", "words", "expected"],
    argvalues=[
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ],
)
def test_func(s: str, words: List[str], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    sub_strings = Solution().findSubstring(s, words)
    assert sub_strings == expected
