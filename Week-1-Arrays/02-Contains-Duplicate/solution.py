# Problem: Contains Duplicate
# Platform: LeetCode
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Date: 23-02-2026

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
