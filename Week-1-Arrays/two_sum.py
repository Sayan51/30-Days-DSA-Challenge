# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Date: 22-02-2026

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
