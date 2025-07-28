import pytest

from awesome_python_leetcode._649_dota2_senate import Solution


@pytest.mark.parametrize(
    argnames=["senate", "expected"],
    argvalues=[
        ("RD", "Radiant"),
        ("RDD", "Dire"),
        ("DDR", "Dire"),
    ],
)
def test_func(senate: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    senator = Solution().predictPartyVictory(senate)
    assert senator == expected
