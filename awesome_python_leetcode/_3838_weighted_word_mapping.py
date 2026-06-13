import string
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        """
        You are given an array of strings words, where each string represents a word
        containing lowercase English letters.

        You are also given an integer array weights of length 26, where weights[i]
        represents the weight of the ith lowercase English letter.

        The weight of a word is defined as the sum of the weights of its characters.

        For each word, take its weight modulo 26 and map the result to a lowercase
        English letter using reverse alphabetical order (0 -> 'z', 1 -> 'y', ...,
        25 -> 'a').

        Return a string formed by concatenating the mapped characters for all
        words in order.
        """
        char_to_num = dict(zip(string.ascii_lowercase, weights, strict=False))
        num_to_char = dict(enumerate(reversed(string.ascii_lowercase)))
        res = ""
        for word in words:
            weight = 0
            for char in word:
                weight += char_to_num[char]
                weight %= 26
            res += num_to_char[weight]
        return res
