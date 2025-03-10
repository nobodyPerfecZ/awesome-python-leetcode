from typing import List

import pytest

from awesome_python_leetcode._49_group_anagrams import Solution


@pytest.mark.parametrize(
    argnames=["strs", "expected"],
    argvalues=[
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_func(strs: List[str], expected: List[List[str]]):
    groups = Solution().groupAnagrams(strs)
    assert groups == expected
