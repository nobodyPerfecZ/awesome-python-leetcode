import pytest

from awesome_python_leetcode._231_power_of_two import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (1, True),
        (16, True),
        (3, False),
    ],
)
def test_func(n: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_power_of_two = Solution().isPowerOfTwo(n)
    assert is_power_of_two is expected
