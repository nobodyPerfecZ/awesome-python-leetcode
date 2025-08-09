from typing import List

import pytest

from awesome_python_leetcode._187_repeated_dna_sequences import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
        ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ],
)
def test_func(s: str, expected: List[str]):
    """Tests the solution of a LeetCode problem."""
    dna_sequences = Solution().findRepeatedDnaSequences(s)
    assert dna_sequences == expected
