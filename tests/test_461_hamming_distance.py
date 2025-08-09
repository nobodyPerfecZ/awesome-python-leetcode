import pytest

from awesome_python_leetcode._461_hamming_distance import Solution


@pytest.mark.parametrize(
    argnames=["x", "y", "expected"],
    argvalues=[
        (1, 4, 2),
        (3, 1, 1),
    ],
)
def test_func(x: int, y: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    hamming_distance = Solution().hammingDistance(x, y)
    assert hamming_distance == expected
