class Solution:
    """Base class for all LeetCode Problems."""

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter
        in pattern and a non-empty word in s.

        Specifically:
        - Each letter in pattern maps to exactly one unique word in s.
        - Each unique word in s maps to exactly one letter in pattern.
        - No two letters map to the same word, and no two words map to the same letter.
        """
        s = s.split()
        if len(pattern) != len(s):
            return False
        policy, reverse_policy = {}, {}
        for pattern_, s_ in zip(pattern, s, strict=True):
            if pattern_ in policy and policy[pattern_] != s_:
                return False
            if s_ in reverse_policy and reverse_policy[s_] != pattern_:
                return False
            policy[pattern_] = s_
            reverse_policy[s_] = pattern_
        return True
