import pytest

from awesome_python_leetcode._12_integer_to_roman import Solution


@pytest.mark.parametrize(
    argnames=["num", "expected"],
    argvalues=[
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_func(num: int, expected: str):
    """Tests the solution of a LeetCode problem."""
    roman = Solution().intToRoman(num)
    assert roman == expected
