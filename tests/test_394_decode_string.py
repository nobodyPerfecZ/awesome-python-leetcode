import pytest

from awesome_python_leetcode._394_decode_string import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ],
)
def test_func(s: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    decoded_s = Solution().decodeString(s)
    assert decoded_s == expected
