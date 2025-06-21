from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        We are given an array asteroids of integers representing asteroids in a row.
        The indices of the asteriod in the array represent their relative position in
        space.

        For each asteroid, the absolute value represents its size, and the sign
        represents its direction (positive meaning right, negative meaning left).
        Each asteroid moves at the same speed.

        Find out the state of the asteroids after all collisions. If two asteroids meet,
        the smaller one will explode. If both are the same size, both will explode.
        Two asteroids moving in the same direction will never meet.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        res = []
        for asteroid in asteroids:
            while res and asteroid < 0 and res[-1] > 0:
                diff = asteroid + res[-1]
                if diff < 0:
                    # abs(asteroid) > abs(res[-1])
                    # res destroyed
                    res.pop()
                elif diff > 0:
                    # abs(asteroid) < abs(res[-1])
                    # asteroid destroyed
                    asteroid = 0
                else:
                    # abs(asteroid) == abs(res[-1])
                    # both destroyed
                    asteroid = 0
                    res.pop()
            if asteroid:
                res.append(asteroid)
        return res
