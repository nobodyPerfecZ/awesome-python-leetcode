from typing import List

import pytest

from awesome_python_leetcode._318_maximum_product_of_word_lengths import Solution


@pytest.mark.parametrize(
    argnames=["words", "expected"],
    argvalues=[
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0),
    ],
)
def test_func(words: List[str], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_product = Solution().maxProduct(words)
    assert max_product == expected
