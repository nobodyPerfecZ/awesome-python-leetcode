class Solution:
    def sum_of_squares(self, n: int) -> int:
        return sum(int(digit) ** 2 for digit in str(abs(n)))

    def isHappy(self, n: int) -> bool:
        """
        Write an algorithm to determine if a number n is happy.

        A happy number is a number defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        - Those numbers for which this process ends in 1 are happy.

        Return true if n is a happy number, and false if not.
        """
        values = {}
        while n != 1:
            if n in values:
                return False
            values[n] = True
            n = self.sum_of_squares(n)
        return True
