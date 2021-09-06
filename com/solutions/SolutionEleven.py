from typing import List


class SolutionEleven:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        h = 0
        length = 0
        while left < right:
            length = right - left
            if height[left] <= height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            s = h * length
            if s > area:
                area = s
        return area
