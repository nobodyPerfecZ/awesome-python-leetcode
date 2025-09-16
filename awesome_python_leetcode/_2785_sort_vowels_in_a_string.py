class Solution:
    """Base class for all LeetCode Problems."""

    def sortVowels(self, s: str) -> str:
        """
        Given a 0-indexed string s, permute s to get a new string t such that:
        - All consonants remain in their original places. More formally, if there is an
        index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
        - The vowels must be sorted in the nondecreasing order of their ASCII values.
        More formally, for pairs of indices i, j with 0 <= i < j < s.length such that
        s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than
        t[j].

        Return the resulting string.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or
        uppercase. Consonants comprise all letters that are not vowels.
        """
        # Get the vowels and position of them
        vowels = [c for c in s if c in "aeiouAEIOU"]

        # Sort the vowels
        vowels.sort()

        # Return the resulting string with sorted vowels
        result = []
        j = 0
        for c in s:
            if c in "aeiouAEIOU":
                result.append(vowels[j])
                j += 1
            else:
                result.append(c)
        return "".join(result)
