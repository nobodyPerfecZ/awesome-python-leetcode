import pytest

from awesome_python_leetcode._165_compare_version_numbers import Solution


@pytest.mark.parametrize(
    argnames=["version1", "version2", "expected"],
    argvalues=[
        ("1.2", "1.10", -1),
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0.0", 0),
    ],
)
def test_func(version1: str, version2: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    compare = Solution().compareVersion(version1, version2)
    assert compare == expected
