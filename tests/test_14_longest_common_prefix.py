from typing import List

import pytest

from awesome_python_leetcode._14_longest_common_prefix import Solution


@pytest.mark.parametrize(
    argnames=["strs", "expected"],
    argvalues=[
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ],
)
def test_func(strs: List[str], expected: str):
    """Tests the solution of a LeetCode problem."""
    prefix = Solution().longestCommonPrefix(strs)
    assert prefix == expected
