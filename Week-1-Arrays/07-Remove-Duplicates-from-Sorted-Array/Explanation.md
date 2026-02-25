---

✅ 7️⃣ Remove Duplicates from Sorted Array

markdown
```
# Intuition
The array is already sorted, which means duplicate elements will always appear next to each other.  
Because of this property, we do not need extra space to remove duplicates.  
We can use a two-pointer approach to shift unique elements forward.

# Approach
1. Handle the edge case where the array is empty.
2. Use two pointers:
   - A slow pointer to track the position of the last unique element.
   - A fast pointer to scan the array.
3. If nums[fast] is different from nums[slow]:
   - Move the slow pointer forward.
   - Copy nums[fast] to nums[slow].
4. Continue until the end of the array.
5. Return slow + 1 as the number of unique elements.

This ensures the first k elements of the array are unique.

# Complexity
- Time complexity: O(n)  
  We traverse the array once.

- Space complexity: O(1)  
  No additional data structures are used.

# Code
```python
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
