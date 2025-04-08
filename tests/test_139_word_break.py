from typing import List

import pytest

from awesome_python_leetcode._139_word_break import Solution


@pytest.mark.parametrize(
    argnames=["s", "wordDict", "expected"],
    argvalues=[
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_func(s: str, wordDict: List[str], expected: bool):
    """Tests the solution of a LeetCode problem."""
    breaked = Solution().wordBreak(s, wordDict)
    assert breaked is expected
