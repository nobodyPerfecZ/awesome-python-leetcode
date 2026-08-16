from functools import lru_cache
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def stoneGame(self, piles: List[int]) -> bool:
        """
        Alice and Bob play a game with piles of stones. There are an even number of
        piles arranged in a row, and each pile has a positive integer number of stones
        piles[i].

        The objective of the game is to end with the most stones. The total number of
        stones across all the piles is odd, so there are no ties.

        Alice and Bob take turns, with Alice starting first. Each turn, a player takes
        the entire pile of stones either from the beginning or from the end of the row.
        This continues until there are no more piles left, at which point the person
        with the most stones wins.

        Assuming Alice and Bob play optimally, return true if Alice wins the game,
        or false if Bob wins.
        """
        N = len(piles)

        @lru_cache(None)
        def dp(left, right):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if left > right:
                return 0
            player1_turn = (right - left - N) % 2
            if player1_turn == 1:  # first player
                return max(
                    piles[left] + dp(left + 1, right),
                    piles[right] + dp(left, right - 1),
                )
            else:
                return min(
                    -piles[left] + dp(left + 1, right),
                    -piles[right] + dp(left, right - 1),
                )

        return dp(0, N - 1) > 0
