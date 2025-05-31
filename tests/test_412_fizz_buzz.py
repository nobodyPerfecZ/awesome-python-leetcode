from typing import List

import pytest

from awesome_python_leetcode._412_fizz_buzz import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_func(n: int, expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    fizzBuzz = Solution().fizzBuzz(n)
    assert fizzBuzz == expected
