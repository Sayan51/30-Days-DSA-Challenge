# Problem 5: Product of Array Except Self
# Platform: LeetCode
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)
# Date: 24-02-2026


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Prefix pass
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
