import pytest

from awesome_python_leetcode._1922_count_good_numbers import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (1, 5),
        (4, 400),
        (50, 564908303),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_good_numbers = Solution().countGoodNumbers(n)
    assert num_good_numbers == expected
