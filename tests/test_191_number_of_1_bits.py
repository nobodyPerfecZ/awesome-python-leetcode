import pytest

from awesome_python_leetcode._191_number_of_1_bits import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (11, 3),
        (128, 1),
        (2147483645, 30),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    c = Solution().hammingWeight(n)
    assert c == expected
