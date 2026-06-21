from typing import List, Tuple


class Solution:
    """Base class for all LeetCode Problems."""

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target
        number (target), find all unique combinations in candidates where the
        candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.
        """
        res = []
        visited = set()

        def dfs(i: int, pair: Tuple[int, ...], total: int):
            if total == target and pair not in visited:
                res.append(pair)
                return
            if i >= len(candidates) or total > target or pair in visited:
                return

            dfs(i + 1, pair + (candidates[i],), total + candidates[i])
            visited.add(pair + (candidates[i],))
            dfs(i + 1, pair, total)
            visited.add(pair)

        candidates = sorted(candidates)
        dfs(0, (), 0)
        return [list(r) for r in res]
