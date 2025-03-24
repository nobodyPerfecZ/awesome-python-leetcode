from typing import List

import pytest

from awesome_python_leetcode._150_evaluate_reverse_polish_notation import Solution


@pytest.mark.parametrize(
    argnames=["tokens", "expected"],
    argvalues=[
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_func(tokens: List[str], expected: int):
    """Tests the solution of a LeetCode problem."""
    value = Solution().evalRPN(tokens)
    assert value == expected
