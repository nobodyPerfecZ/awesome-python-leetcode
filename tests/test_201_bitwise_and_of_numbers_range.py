import pytest

from awesome_python_leetcode._201_bitwise_and_of_numbers_range import Solution


@pytest.mark.parametrize(
    argnames=["left", "right", "expected"],
    argvalues=[
        (5, 7, 4),
        (0, 0, 0),
        (1, 2147483647, 0),
    ],
)
def test_func(left: int, right: int, expected: int):
    range_bitwise_and = Solution().rangeBitwiseAnd(left, right)
    assert range_bitwise_and == expected
