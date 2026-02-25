# Problem: Remove Duplicates from Sorted Array
# Platform: LeetCode
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)
# Day: 07
# Date: 25-02-2026

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1
