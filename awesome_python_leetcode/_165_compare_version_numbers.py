class Solution:
    """Base class for all LeetCode Problems."""

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Given two version strings, version1 and version2, compare them. A version
        string consists of revisions separated by dots '.'. The value of the revision
        is its integer conversion ignoring leading zeros.

        To compare version strings, compare their revision values in left-to-right
        order. If one of the version strings has fewer revisions, treat the missing
        revision values as 0.

        Return the following:
        - If version1 < version2, return -1.
        - If version1 > version2, return 1.
        - Otherwise, return 0.
        """
        numbers1 = list(map(int, version1.split(".")))
        numbers2 = list(map(int, version2.split(".")))
        i, j = 0, 0
        while i < len(numbers1) or j < len(numbers2):
            number1 = 0 if i >= len(numbers1) else numbers1[i]
            number2 = 0 if j >= len(numbers2) else numbers2[j]

            if number1 < number2:
                return -1

            if number1 > number2:
                return 1

            i += 1
            j += 1

        return 0
