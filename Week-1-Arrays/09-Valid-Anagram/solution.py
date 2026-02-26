# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Day: 09
# Date: 26-02-2026

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
