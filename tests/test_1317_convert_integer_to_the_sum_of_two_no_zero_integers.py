from typing import List

import pytest

from awesome_python_leetcode._1317_convert_integer_to_the_sum_of_two_no_zero_integers import (  # noqa: E501
    Solution,
)


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, [1, 1]),
        (11, [6, 5]),
        (1010, [499, 511]),
        (19, [8, 11]),
        (2081, [969, 1112]),
    ],
)
def test_func(n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    zero_integers = Solution().getNoZeroIntegers(n)
    assert zero_integers == expected
