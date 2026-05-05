# Problem: Two Sum II – Input Array Is Sorted
# Technique: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        
        return []