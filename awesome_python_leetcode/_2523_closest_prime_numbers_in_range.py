from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def getPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for i in range(right + 1)]
        primes[0] = primes[1] = False
        p = 2
        while p * p < right + 1:
            if primes[p]:
                for i in range(p * p, right + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(left, right + 1) if primes[i]]

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.getPrimes(left, right)

        if len(primes) < 2:
            return [-1, -1]
        if len(primes) == 2:
            return primes

        prime1 = primes[0]
        prime2 = primes[1]
        for i in range(0, len(primes) - 1):
            if primes[i + 1] - primes[i] < prime2 - prime1:
                prime1 = primes[i]
                prime2 = primes[i + 1]
        return [prime1, prime2]
