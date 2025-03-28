from typing import List

import pytest

from awesome_python_leetcode._200_number_of_islands import Solution


@pytest.mark.parametrize(
    argnames=["grid", "expected"],
    argvalues=[
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_func(grid: List[List[str]], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_islands = Solution().numIslands(grid)
    assert num_islands == expected
