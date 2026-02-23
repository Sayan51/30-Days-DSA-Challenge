# ✅ 2️⃣ Contains Duplicate

```markdown
# Intuition
The problem asks whether any number appears more than once in the array.  
If all elements are unique, the length of the array and the length of a set created from it will be the same.  
Since sets automatically remove duplicates, this gives us a simple and efficient way to check.

# Approach
1. Convert the list into a set.
2. Compare the length of the original list with the set.
3. If the lengths differ, duplicates exist.
4. Otherwise, all elements are unique.

This avoids brute force comparison and runs efficiently.

# Complexity
- Time complexity: O(n)  
  Creating a set takes linear time.

- Space complexity: O(n)  
  In the worst case, all elements are stored in the set.

# Code
```python
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
