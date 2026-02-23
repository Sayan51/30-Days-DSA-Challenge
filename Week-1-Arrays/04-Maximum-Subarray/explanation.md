
---

# ✅ 4️⃣ Maximum Subarray (Kadane’s Algorithm)

```markdown
# Intuition
We need to find a contiguous subarray with the maximum sum.  
At each index, we decide whether to:
- Start a new subarray from the current element
- Or extend the previous subarray

If the running sum becomes harmful (negative), starting fresh is better.

# Approach
1. Initialize `current_sum` and `max_sum` with the first element.
2. Traverse from index 1:
   - Update `current_sum` as max(current element, current_sum + element)
   - Update `max_sum` if current_sum is larger.
3. Return `max_sum`.

This is Kadane’s Algorithm.

# Complexity
- Time complexity: O(n)  
  Single pass through the array.

- Space complexity: O(1)  
  No extra data structures used.

# Code
```python
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
