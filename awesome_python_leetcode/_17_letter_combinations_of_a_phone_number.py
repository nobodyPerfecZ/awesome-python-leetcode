from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given
        below. Note that 1 does not map to any letters.
        """
        res = []
        digitToLetter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(i: int, word: str):
            if len(word) == len(digits):
                res.append(word)
                return

            letters = digitToLetter[digits[i]]
            for c in letters:
                dfs(i + 1, word + c)

        if digits:
            dfs(0, "")
        return res
