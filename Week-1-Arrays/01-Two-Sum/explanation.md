# ✅ 1️⃣ Two Sum

```markdown
# Intuition
The problem asks us to find two numbers in the array whose sum equals a given target.

A brute-force approach would check every pair of elements, which would take O(n²) time.

Instead, we can use a hash map to store numbers we have already seen.  
For each number, we calculate the complement needed to reach the target.  
If that complement already exists in the hash map, we have found our answer.

---

# Approach

1. Create an empty hash map (dictionary).
2. Traverse the array using enumerate to get both index and value.
3. For each number:
   - Compute complement = target - num
   - Check if complement exists in the hash map.
   - If yes, return the stored index and current index.
4. Otherwise, store the current number and its index in the hash map.
5. Continue until a solution is found.

This guarantees a single pass through the array.

---

# Complexity

- Time Complexity: O(n)  
  We traverse the array once and each lookup in the hash map is O(1).

- Space Complexity: O(n)  
  In the worst case, we store all elements in the hash map.

---

# Code

```python
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
