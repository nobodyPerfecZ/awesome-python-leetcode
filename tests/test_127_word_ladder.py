from typing import List

import pytest

from awesome_python_leetcode._127_word_ladder import Solution


@pytest.mark.parametrize(
    argnames=["beginWord", "endWord", "wordList", "expected"],
    argvalues=[
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
)
def test_func(beginWord: str, endWord: str, wordList: List[str], expected: int):
    """Tests the solution of a LeetCode problem."""
    sequence_length = Solution().ladderLength(beginWord, endWord, wordList)
    assert sequence_length == expected
