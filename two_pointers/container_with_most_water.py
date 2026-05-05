# Problem: Container With Most Water
# Technique: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, h * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area