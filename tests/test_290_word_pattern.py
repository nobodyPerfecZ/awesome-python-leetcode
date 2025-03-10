import pytest

from awesome_python_leetcode._290_word_pattern import Solution


@pytest.mark.parametrize(
    argnames=["pattern", "s", "expected"],
    argvalues=[
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ],
)
def test_func(pattern: str, s: str, expected: bool):
    word_pattern = Solution().wordPattern(pattern, s)
    assert word_pattern == expected
