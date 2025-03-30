import pytest

from awesome_python_leetcode._6_zigzag_conversion import Solution


@pytest.mark.parametrize(
    argnames=["s", "numRows", "expected"],
    argvalues=[
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("ABC", 1, "ABC"),
    ],
)
def test_func(s: str, numRows: int, expected: str):
    """Tests the solution of a LeetCode problem."""
    zigzag = Solution().convert(s, numRows)
    assert zigzag == expected
