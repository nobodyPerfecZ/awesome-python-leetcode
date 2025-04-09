import pytest

from awesome_python_leetcode._72_edit_distance import Solution


@pytest.mark.parametrize(
    argnames=["word1", "word2", "expected"],
    argvalues=[
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ],
)
def test_func(word1: str, word2: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    distance = Solution().minDistance(word1, word2)
    assert distance == expected
