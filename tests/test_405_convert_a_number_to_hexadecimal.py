import pytest

from awesome_python_leetcode._405_convert_a_number_to_hexadecimal import Solution


@pytest.mark.parametrize(
    argnames=["num", "expected"],
    argvalues=[
        (26, "1a"),
        (-1, "ffffffff"),
        (0, "0"),
    ],
)
def test_func(num: int, expected: str):
    """Tests the solution of a LeetCode problem."""
    hex_code = Solution().toHex(num)
    assert hex_code == expected
