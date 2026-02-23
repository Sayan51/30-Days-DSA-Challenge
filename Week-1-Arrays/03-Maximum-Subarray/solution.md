# Problem: Maximum Subarray
# Platform: LeetCode
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)
# Date: 23-02-2026

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
