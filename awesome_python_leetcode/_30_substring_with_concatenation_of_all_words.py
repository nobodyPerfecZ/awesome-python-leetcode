import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        You are given a string s and an array of strings words. All the strings of
        words are of the same length.

        A concatenated string is a string that exactly contains all the strings of any
        permutation of words concatenated.

        - For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
        "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not
        a concatenated string because it is not the concatenation of any permutation
        of words.

        Return an array of the starting indices of all the concatenated substrings in s.
        You can return the answer in any order.
        """
        needCount = collections.defaultdict(int)
        res = []

        for word in words:
            needCount[word] += 1

        wordLen = len(words[0])
        windowLen = len(words) * wordLen
        for left in range(len(s) - windowLen + 1):
            haveCount = collections.defaultdict(int)
            right = left

            while right < left + windowLen:
                word = s[right : right + wordLen]

                if word not in needCount:
                    break

                haveCount[word] += 1

                if haveCount[word] > needCount[word]:
                    break

                right += wordLen

            if right == left + windowLen:
                res.append(left)
        return res
