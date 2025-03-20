from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def jump(self, nums: List[int]) -> int:
        """
        You are given a 0-indexed array of integers nums of length n. You are initially
        positioned at nums[0].

        Each element nums[i] represents the maximum length of a forward jump from index
        i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
        - 0 <= j <= nums[i] and i + j < n

        Return the minimum number of jumps to reach nums[n - 1]. The test cases are
        generated such that you can reach nums[n - 1].
        """

        left, right, jumps = 0, 0, 0
        while right < len(nums) - 1:
            largest_jump = 0
            for i in range(left, right + 1):
                largest_jump = max(largest_jump, i + nums[i])
            left = right + 1
            right = largest_jump
            jumps += 1
        return jumps
