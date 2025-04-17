import pytest

from awesome_python_leetcode._91_decode_ways import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    decodings = Solution().numDecodings(s)
    assert decodings == expected
