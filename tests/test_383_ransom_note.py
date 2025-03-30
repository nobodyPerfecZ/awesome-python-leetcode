import pytest

from awesome_python_leetcode._383_ransom_note import Solution


@pytest.mark.parametrize(
    argnames=["ransomNote", "magazine", "expected"],
    argvalues=[
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ],
)
def test_func(ransomNote: str, magazine: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    can_construct = Solution().canConstruct(ransomNote, magazine)
    assert can_construct is expected
