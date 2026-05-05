# Problem: Ransom Note
# Technique: Counting
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26
        
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            if count[ord(c) - ord('a')] == 0:
                return False
            count[ord(c) - ord('a')] -= 1
        
        return True