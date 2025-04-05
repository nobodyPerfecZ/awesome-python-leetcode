from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers
        sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two
        combinations are unique if the frequency of at least one of the chosen numbers
        is different.

        The test cases are generated such that the number of unique combinations that
        sum up to target is less than 150 combinations for the given input.
        """
        res = []

        def dfs(i: int, pair: List[int], total: int):
            if total == target:
                res.append(pair.copy())
                return
            if i >= len(candidates) or total > target:
                return

            pair.append(candidates[i])
            dfs(i, pair, total + candidates[i])
            pair.pop()
            dfs(i + 1, pair, total)

        dfs(0, [], 0)
        return res
