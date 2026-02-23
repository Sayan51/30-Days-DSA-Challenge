
---

# ✅ 3️⃣ Best Time to Buy and Sell Stock

```markdown
# Intuition
We want to maximize profit by buying once and selling once.  
Instead of checking every pair of days (which would be O(n²)), we track the minimum price seen so far and calculate profit at each step.

If selling today gives better profit than before, we update the maximum profit.

# Approach
1. Initialize `min_price` as infinity.
2. Initialize `max_profit` as 0.
3. Traverse through prices:
   - Update `min_price` if current price is lower.
   - Otherwise, compute profit and update `max_profit`.
4. Return `max_profit`.

This ensures a single pass through the array.

# Complexity
- Time complexity: O(n)  
  Only one traversal is required.

- Space complexity: O(1)  
  Only two variables are used.

# Code
```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
