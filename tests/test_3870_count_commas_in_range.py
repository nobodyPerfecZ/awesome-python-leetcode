import pytest

from awesome_python_leetcode._3870_count_commas_in_range import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (1002, 3),
        (998, 0),
        (100000, 99001),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    count_commas = Solution().countCommas(n)
    assert count_commas == expected
