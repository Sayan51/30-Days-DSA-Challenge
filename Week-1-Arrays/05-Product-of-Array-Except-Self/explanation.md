---

✅ 5️⃣ Product of Array Except Self

```markdown
# Intuition
For every index, we need the product of all elements except itself.

Instead of dividing the total product (which fails with zeros and is not allowed),
we split the problem into two parts:
- Product of elements to the left
- Product of elements to the right

If we multiply left product and right product,
we get the required answer.

# Approach
1. Create an output array initialized with 1.
2. Traverse from left to right:
   - Store prefix product (product of elements before index i).
3. Traverse from right to left:
   - Multiply each index with suffix product (product of elements after index i).
4. Return the result array.

This avoids division and uses constant extra space.

# Complexity
- Time complexity: O(n)  
  Two linear passes through the array.

- Space complexity: O(1)  
  Only output array is used (not counted as extra space).

# Code
```python
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
