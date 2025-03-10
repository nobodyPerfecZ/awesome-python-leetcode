from typing import List

import pytest

from awesome_python_leetcode._228_summary_ranges import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ],
)
def test_func(nums: List[int], expected: List[str]):
    ranges = Solution().summaryRanges(nums)
    assert ranges == expected
