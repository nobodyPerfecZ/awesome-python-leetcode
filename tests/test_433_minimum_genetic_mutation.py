from typing import List

import pytest

from awesome_python_leetcode._433_minimum_genetic_mutation import Solution


@pytest.mark.parametrize(
    argnames=["startGene", "endGene", "bank", "expected"],
    argvalues=[
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
    ],
)
def test_func(startGene: str, endGene: str, bank: List[str], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_mutations = Solution().minMutation(startGene, endGene, bank)
    assert num_mutations == expected
