import collections


class Solution:
    """Base class for all LeetCode Problems."""

    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum
        window substring of s such that every character in t (including duplicates) is
        included in the window. If there is no such substring, return the empty
        string "".

        The testcases will be generated such that the answer is unique.
        """
        if len(s) < len(t):
            return ""

        haveCount = collections.defaultdict(int)
        needCount = collections.defaultdict(int)
        for c in t:
            needCount[c] += 1

        have, need = 0, len(needCount)
        res, resLen = [-1, -1], float("infinity")
        left, right = 0, 0
        while left < len(s) and right < len(s):
            c = s[right]
            haveCount[c] += 1
            if c in needCount and haveCount[c] == needCount[c]:
                have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                c = s[left]
                haveCount[c] -= 1
                if c in needCount and haveCount[c] < needCount[c]:
                    have -= 1
                left += 1
            right += 1
        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""
