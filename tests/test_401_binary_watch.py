from typing import List

import pytest

from awesome_python_leetcode._401_binary_watch import Solution


@pytest.mark.parametrize(
    argnames=["turnedOn", "expected"],
    argvalues=[
        (
            1,
            [
                "0:08",
                "0:04",
                "0:16",
                "0:02",
                "0:01",
                "0:32",
                "4:00",
                "2:00",
                "1:00",
                "8:00",
            ],
        ),
        (9, []),
        (0, ["0:00"]),
    ],
)
def test_func(turnedOn: int, expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    possible_times = Solution().readBinaryWatch(turnedOn)
    assert possible_times == expected
