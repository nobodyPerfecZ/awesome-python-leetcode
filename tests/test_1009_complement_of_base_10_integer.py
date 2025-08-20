import pytest

from awesome_python_leetcode._1009_complement_of_base_10_integer import Solution


@pytest.mark.parametrize(
    argnames=["num", "expected"],
    argvalues=[
        (5, 2),
        (7, 0),
        (10, 5),
        (0, 1),
    ],
)
def test_func(num: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    complement = Solution().bitwiseComplement(num)
    assert complement == expected
