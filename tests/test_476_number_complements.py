import pytest

from awesome_python_leetcode._476_number_complement import Solution


@pytest.mark.parametrize(
    argnames=["num", "expected"],
    argvalues=[
        (5, 2),
        (1, 0),
        (0, 1),
    ],
)
def test_func(num: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    complement = Solution().findComplement(num)
    assert complement == expected
