class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An anagram is a word or phrase formed by rearranging the letters of a different word
        or phrase, using all the original letters exactly once.
        """
        if len(s) != len(t):
            return False

        counter_s, counter_t = {}, {}
        for s_, t_ in zip(s, t):
            if s_ not in counter_s:
                counter_s[s_] = 1
            else:
                counter_s[s_] += 1

            if t_ not in counter_t:
                counter_t[t_] = 1
            else:
                counter_t[t_] += 1

        for k_s, k_t in zip(counter_s, counter_t):
            if k_s not in counter_t:
                return False
            if k_t not in counter_s:
                return False
            if counter_s[k_s] != counter_t[k_s] or counter_s[k_t] != counter_t[k_t]:
                return False
        return True
