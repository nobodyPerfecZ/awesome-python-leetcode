import pytest

from awesome_python_leetcode._790_domino_and_tromino_tiling import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (3, 5),
        (1, 1),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().numTilings(n)
    assert two_sum == expected
