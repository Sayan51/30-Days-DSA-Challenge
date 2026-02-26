# Problem: Group Anagrams
# Platform: LeetCode
# Difficulty: Medium
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
# Day: 10
# Date: 26-02-2026

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)
        
        return list(groups.values())
