class Solution:
    """Base class for all LeetCode Problems."""

    def addStrings(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers, num1 and num2 represented as string, return the
        sum of num1 and num2 as a string.

        You must solve the problem without using any built-in library for handling large
        integers (such as BigInteger). You must also not convert the inputs to integers
        directly.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Addition Rules (num1, num2) => (res, rem)
        RULES = {
            ("0", "0"): ("0", "0"),
            ("0", "1"): ("1", "0"),
            ("0", "2"): ("2", "0"),
            ("0", "3"): ("3", "0"),
            ("0", "4"): ("4", "0"),
            ("0", "5"): ("5", "0"),
            ("0", "6"): ("6", "0"),
            ("0", "7"): ("7", "0"),
            ("0", "8"): ("8", "0"),
            ("0", "9"): ("9", "0"),
            ("1", "0"): ("1", "0"),
            ("1", "1"): ("2", "0"),
            ("1", "2"): ("3", "0"),
            ("1", "3"): ("4", "0"),
            ("1", "4"): ("5", "0"),
            ("1", "5"): ("6", "0"),
            ("1", "6"): ("7", "0"),
            ("1", "7"): ("8", "0"),
            ("1", "8"): ("9", "0"),
            ("1", "9"): ("0", "1"),
            ("2", "0"): ("2", "0"),
            ("2", "1"): ("3", "0"),
            ("2", "2"): ("4", "0"),
            ("2", "3"): ("5", "0"),
            ("2", "4"): ("6", "0"),
            ("2", "5"): ("7", "0"),
            ("2", "6"): ("8", "0"),
            ("2", "7"): ("9", "0"),
            ("2", "8"): ("0", "1"),
            ("2", "9"): ("1", "1"),
            ("3", "0"): ("3", "0"),
            ("3", "1"): ("4", "0"),
            ("3", "2"): ("5", "0"),
            ("3", "3"): ("6", "0"),
            ("3", "4"): ("7", "0"),
            ("3", "5"): ("8", "0"),
            ("3", "6"): ("9", "0"),
            ("3", "7"): ("0", "1"),
            ("3", "8"): ("1", "1"),
            ("3", "9"): ("2", "1"),
            ("4", "0"): ("4", "0"),
            ("4", "1"): ("5", "0"),
            ("4", "2"): ("6", "0"),
            ("4", "3"): ("7", "0"),
            ("4", "4"): ("8", "0"),
            ("4", "5"): ("9", "0"),
            ("4", "6"): ("0", "1"),
            ("4", "7"): ("1", "1"),
            ("4", "8"): ("2", "1"),
            ("4", "9"): ("3", "1"),
            ("5", "0"): ("5", "0"),
            ("5", "1"): ("6", "0"),
            ("5", "2"): ("7", "0"),
            ("5", "3"): ("8", "0"),
            ("5", "4"): ("9", "0"),
            ("5", "5"): ("0", "1"),
            ("5", "6"): ("1", "1"),
            ("5", "7"): ("2", "1"),
            ("5", "8"): ("3", "1"),
            ("5", "9"): ("4", "1"),
            ("6", "0"): ("6", "0"),
            ("6", "1"): ("7", "0"),
            ("6", "2"): ("8", "0"),
            ("6", "3"): ("9", "0"),
            ("6", "4"): ("0", "1"),
            ("6", "5"): ("1", "1"),
            ("6", "6"): ("2", "1"),
            ("6", "7"): ("3", "1"),
            ("6", "8"): ("4", "1"),
            ("6", "9"): ("5", "1"),
            ("7", "0"): ("7", "0"),
            ("7", "1"): ("8", "0"),
            ("7", "2"): ("9", "0"),
            ("7", "3"): ("0", "1"),
            ("7", "4"): ("1", "1"),
            ("7", "5"): ("2", "1"),
            ("7", "6"): ("3", "1"),
            ("7", "7"): ("4", "1"),
            ("7", "8"): ("5", "1"),
            ("7", "9"): ("6", "1"),
            ("8", "0"): ("8", "0"),
            ("8", "1"): ("9", "0"),
            ("8", "2"): ("0", "1"),
            ("8", "3"): ("1", "1"),
            ("8", "4"): ("2", "1"),
            ("8", "5"): ("3", "1"),
            ("8", "6"): ("4", "1"),
            ("8", "7"): ("5", "1"),
            ("8", "8"): ("6", "1"),
            ("8", "9"): ("7", "1"),
            ("9", "0"): ("9", "0"),
            ("9", "1"): ("0", "1"),
            ("9", "2"): ("1", "1"),
            ("9", "3"): ("2", "1"),
            ("9", "4"): ("3", "1"),
            ("9", "5"): ("4", "1"),
            ("9", "6"): ("5", "1"),
            ("9", "7"): ("6", "1"),
            ("9", "8"): ("7", "1"),
            ("9", "9"): ("8", "1"),
        }

        # Get the smallest and largest number
        if len(num1) <= len(num2):
            smallest = num1
            largest = num2
        else:
            smallest = num2
            largest = num1

        # Add leading zeros to the smallest number
        smallest = "0" * (len(largest) - len(smallest)) + smallest

        # Loop through the digits from right to left
        result = ""
        remaining = "0"
        for n1, n2 in zip(reversed(smallest), reversed(largest)):
            # Apply the addition rules including remaining
            add, next_remaining1 = RULES[(n1, n2)]
            add, next_remaining2 = RULES[(add, remaining)]

            # Determine the next remaining value
            if next_remaining1 == "1":
                next_remaining = next_remaining1
            else:
                next_remaining = next_remaining2

            # Update the result and remaining
            result = add + result
            remaining = next_remaining

        # Add the remaining value if it's not zero
        if remaining == "1":
            result = remaining + result

        return result
