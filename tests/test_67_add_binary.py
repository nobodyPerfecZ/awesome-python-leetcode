import pytest

from awesome_python_leetcode._67_add_binary import Solution


@pytest.mark.parametrize(
    argnames=["a", "b", "expected"],
    argvalues=[
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
    ],
)
def test_func(a: str, b: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    c = Solution().addBinary(a, b)
    assert c == expected
