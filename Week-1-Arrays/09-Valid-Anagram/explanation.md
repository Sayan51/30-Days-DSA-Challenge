
----

# ✅ 9️⃣ Valid Anagram

```markdown
# Intuition
Two strings are anagrams if they contain the same characters with the same frequency.  
Since the order of characters does not matter, we only need to compare their character counts.

If both strings have identical frequency distributions, they are anagrams.

# Approach
1. First, check if the lengths of both strings are equal.
   - If not, return False immediately.
2. Create a dictionary to store character frequencies from string `s`.
3. Traverse string `s` and increase the count of each character.
4. Traverse string `t`:
   - If a character does not exist in the dictionary, return False.
   - Decrease its count.
   - If the count becomes negative, return False.
5. If all characters match correctly, return True.

This avoids sorting and ensures a linear time solution.

# Complexity
- Time complexity: O(n)  
  We traverse both strings once.

- Space complexity: O(n)  
  In the worst case, we store all unique characters in the dictionary.

# Code
```python
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1
            
            if count[char] < 0:
                return False
        
        return True
