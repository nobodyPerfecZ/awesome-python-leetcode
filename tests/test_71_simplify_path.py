import pytest

from awesome_python_leetcode._71_simplify_path import Solution


@pytest.mark.parametrize(
    argnames=["path", "expected"],
    argvalues=[
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        ("/a/./b/../../c/", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
    ],
)
def test_func(path: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    simplified_path = Solution().simplifyPath(path)
    assert simplified_path == expected
