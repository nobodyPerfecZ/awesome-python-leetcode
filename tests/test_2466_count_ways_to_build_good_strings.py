import pytest

from awesome_python_leetcode._2466_count_ways_to_build_good_strings import Solution


@pytest.mark.parametrize(
    argnames=["low", "high", "zero", "one", "expected"],
    argvalues=[
        (3, 3, 1, 1, 8),
        (2, 3, 1, 2, 5),
    ],
)
def test_func(low: int, high: int, zero: int, one: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    good_strings = Solution().countGoodStrings(low, high, zero, one)
    assert good_strings == expected
