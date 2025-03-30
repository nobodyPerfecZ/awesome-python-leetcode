import pytest

from awesome_python_leetcode._242_valid_anagram import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[("anagram", "nagaram", True), ("rat", "car", False)],
)
def test_func(s: str, t: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_anagram = Solution().isAnagram(s, t)
    assert is_anagram is expected
