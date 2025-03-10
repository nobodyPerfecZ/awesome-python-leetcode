class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character, but a character may map to itself.
        """
        if len(s) != len(t):
            return False
        policy, reverse_policy = {}, {}
        for s_, t_ in zip(s, t):
            if s_ in policy and policy[s_] != t_:
                return False
            if t_ in reverse_policy and reverse_policy[t_] != s_:
                return False
            policy[s_] = t_
            reverse_policy[t_] = s_
        return True
