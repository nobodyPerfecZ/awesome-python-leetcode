import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def hIndex(self, citations: List[int]) -> int:
        """
        Given an array of integers citations where citations[i] is the number of
        citations a researcher received for their ith paper, return the researcher's
        h-index.

        According to the definition of h-index on Wikipedia: The h-index is defined as
        the maximum value of h such that the given researcher has published at least h
        papers that have each been cited at least h times.
        """
        # Sort citations by number of papers
        n = len(citations)
        count = collections.defaultdict(int)
        for i, val in enumerate(citations):
            index = min(val, n)
            count[index] += 1

        # Find index h that have at least h paper with more than h citations
        num_paper = 0
        for h_index in range(n, -1, -1):
            num_paper += count[h_index]
            if num_paper >= h_index:
                return h_index
