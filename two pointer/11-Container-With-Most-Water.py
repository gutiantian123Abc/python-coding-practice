"""
11. Container With Most Water
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) <= 1:
            return 0

        max_vol = 0

        left, right = 0, len(height) - 1
        while left < right:
            left_height, right_height = height[left], height[right]
            max_vol = max(max_vol, (right - left) * min(left_height, right_height))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_vol