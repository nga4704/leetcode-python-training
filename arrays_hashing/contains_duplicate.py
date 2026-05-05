# Problem: Contains Duplicate
# Technique: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Idea:
# - Duyệt mảng
# - Nếu phần tử đã tồn tại trong set → có duplicate
# - Nếu chưa → thêm vào set

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False