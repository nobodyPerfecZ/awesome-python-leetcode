class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
        removing all non-alphanumeric characters, it reads the same forward and backward.
        Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if (s[left] < "a" or s[left] > "z") and (s[left] < "0" or s[left] > "9"):
                left += 1
            elif (s[right] < "a" or s[right] > "z") and (
                s[right] < "0" or s[right] > "9"
            ):
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
