from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def candy(self, ratings: List[int]) -> int:
        """
        There are n children standing in a line. Each child is assigned a rating value
        given in the integer array ratings.

        You are giving candies to these children subjected to the following
        requirements:
        - Each child must have at least one candy.
        - Children with a higher rating get more candies than their neighbors.
        - Return the minimum number of candies you need to have to distribute the
        candies to the children.
        """
        candy = [1 for i in range(len(ratings))]

        # From left to right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = max(candy[i], candy[i - 1]) + 1

        # From right to left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = max(candy[i], candy[i + 1]) + 1
        return sum(candy)
