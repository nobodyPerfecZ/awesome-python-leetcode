from typing import List

import pytest

from awesome_python_leetcode._22_generate_parentheses import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ],
)
def test_func(n: int, expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().generateParenthesis(n)
    assert combinations == expected
