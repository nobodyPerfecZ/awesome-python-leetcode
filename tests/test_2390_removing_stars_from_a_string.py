import pytest

from awesome_python_leetcode._2390_removing_stars_from_a_string import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[("leet**cod*e", "lecoe"), ("erase*****", ""), ("abb*cdfg*****x*", "a")],
)
def test_func(s: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    removed_stars = Solution().removeStars(s)
    assert removed_stars == expected
