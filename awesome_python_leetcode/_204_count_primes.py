class Solution:
    """Base class for all LeetCode Problems."""

    def countPrimes(self, n: int) -> int:
        """
        Given an integer n, return the number of prime numbers that are strictly less
        than n.
        """
        # Time Complexity: O(n*sqrt(n))
        # Space Complexity: O(n)
        if n == 0 or n == 1:
            return 0
        primes = [True for i in range(n)]
        primes[0] = primes[1] = False
        p = 2
        while p * p < n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        return sum(primes)
