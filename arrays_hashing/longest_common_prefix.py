# Problem: Longest Common Prefix
# Technique: Horizontal Scanning
# Time Complexity: O(n * m)
# n = number of strings, m = length of shortest string
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            # rút ngắn prefix cho tới khi s bắt đầu bằng prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix