from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left, right = 0, len(height) - 1
        while left < right:
            if ((potential_score := min(height[left], height[right]) * (right - left)) > best):
                best = potential_score
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best
