import pytest

from awesome_python_leetcode._97_interleaving_string import Solution


@pytest.mark.parametrize(
    argnames=["s1", "s2", "s3", "expected"],
    argvalues=[
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
def test_func(s1: str, s2: str, s3: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    interleave = Solution().isInterleave(s1, s2, s3)
    assert interleave is expected
