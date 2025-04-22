import pytest

from awesome_python_leetcode._96_unique_binary_search_trees import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (3, 5),
        (1, 1),
        (6, 132),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    num_bsts = Solution().numTrees(n)
    assert num_bsts == expected
