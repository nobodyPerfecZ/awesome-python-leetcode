class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed
        by using the letters from magazine and false otherwise.

        Each letter in magazine can only be used once in ransomNote.
        """
        # Count letters from ransomNote
        counter_r = {}
        for s in ransomNote:
            if s not in counter_r:
                counter_r[s] = 1
            else:
                counter_r[s] += 1

        # Count letters from magazine
        counter_m = {}
        for s in magazine:
            if s not in counter_m:
                counter_m[s] = 1
            else:
                counter_m[s] += 1

        # Compare both counts
        for k in counter_r:
            if k not in counter_m or counter_r[k] > counter_m[k]:
                return False
        return True
