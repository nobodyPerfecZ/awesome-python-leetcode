from typing import List

import pytest

from awesome_python_leetcode._79_word_search import Solution


@pytest.mark.parametrize(
    argnames=["board", "word", "expected"],
    argvalues=[
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ],
)
def test_func(board: List[List[str]], word: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    exist = Solution().exist(board, word)
    assert exist is expected
