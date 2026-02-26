
---

# 🔟 Group Anagrams

```markdown
# Intuition

Two words are anagrams if they contain the same characters arranged in different orders.

If we sort the characters of two anagram words, the sorted result will be identical.

For example:
- "eat" → "aet"
- "tea" → "aet"
- "ate" → "aet"

So we can use the sorted string as a unique key to group anagrams.

---

# Approach

1. Create an empty dictionary to store groups.
2. Traverse each word in the list.
3. Sort the characters of the word.
4. Join the sorted characters to form a key.
5. If the key does not exist in the dictionary, create a new list.
6. Append the word to the corresponding key group.
7. Return all grouped values.

This ensures all anagrams share the same key.

---

# Complexity

- Time complexity: O(n * k log k)  
  Where n is the number of words and k is the maximum length of each word.  
  Sorting each word takes O(k log k).

- Space complexity: O(n * k)  
  We store all words inside the dictionary groups.

---

# Code

```python
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)
        
        return list(groups.values())
