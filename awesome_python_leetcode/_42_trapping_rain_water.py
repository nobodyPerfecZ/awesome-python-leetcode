from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of
        each bar is 1, compute how much water it can trap after raining.
        """
        water = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
        return water
