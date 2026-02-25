
---

# ✅ 8️⃣ Merge Sorted Array

```markdown
# Intuition
Both arrays are already sorted.  
If we try to merge from the front, we risk overwriting values in nums1.  
Instead, merging from the back allows us to place the largest elements safely without losing data.

# Approach
1. Initialize three pointers:
   - p1 at the last valid element of nums1.
   - p2 at the last element of nums2.
   - p at the last position of nums1.
2. Compare nums1[p1] and nums2[p2].
3. Place the larger element at index p.
4. Move the corresponding pointer backward.
5. If nums2 still has remaining elements, copy them into nums1.

This allows in-place merging without extra space.

# Complexity
- Time complexity: O(m + n)  
  Each element from both arrays is processed once.

- Space complexity: O(1)  
  The merge is done in-place.

# Code
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
