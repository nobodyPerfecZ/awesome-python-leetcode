from typing import List

import pytest

from awesome_python_leetcode._212_word_search_II import Solution


@pytest.mark.parametrize(
    argnames=["board", "words", "expected"],
    argvalues=[
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
    ],
)
def test_func(board: List[List[str]], words: List[str], expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    words_founded = Solution().findWords(board, words)
    assert set(words_founded) == set(expected)
