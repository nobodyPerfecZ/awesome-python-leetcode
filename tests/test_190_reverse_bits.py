import pytest

from awesome_python_leetcode._190_reverse_bits import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (0b00000010100101000001111010011100, 0b00111001011110000010100101000000),
        (0b11111111111111111111111111111101, 0b10111111111111111111111111111111),
    ],
)
def test_func(n: int, expected: int):
    n_reversed = Solution().reverseBits(n)
    assert n_reversed == expected
