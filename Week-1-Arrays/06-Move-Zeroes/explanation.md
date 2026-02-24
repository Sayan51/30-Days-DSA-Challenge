
---

# ✅ 6️⃣ Move Zeroes

```markdown
# Intuition
We need to move all zeroes to the end while maintaining
the relative order of non-zero elements.

Instead of shifting elements repeatedly,
we can compact all non-zero elements forward.

We use two pointers:
- One pointer to scan the array
- One pointer to place the next non-zero element

# Approach
1. Initialize `left = 0`.
2. Traverse the array using `right`.
3. Whenever nums[right] is not zero:
   - Swap nums[left] and nums[right].
   - Increment left.
4. Continue until the end of the array.

This pushes zeroes to the end while preserving order.

# Complexity
- Time complexity: O(n)  
  Single pass through the array.

- Space complexity: O(1)  
  In-place modification.

# Code
```python
class Solution(object):
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
