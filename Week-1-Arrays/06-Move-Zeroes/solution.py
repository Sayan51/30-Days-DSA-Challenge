# Problem 6: Move Zeroes
# Platform: LeetCode
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)
# Date: 24-02-2026


class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
