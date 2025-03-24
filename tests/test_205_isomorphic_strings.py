import pytest

from awesome_python_leetcode._205_isomorphic_strings import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[("egg", "add", True), ("foo", "bar", False), ("paper", "title", True)],
)
def test_func(s: str, t: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_isomorphic = Solution().isIsomorphic(s, t)
    assert is_isomorphic == expected
