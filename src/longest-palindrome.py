"""
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
"""
import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if s == None or size < 1:
            return ""
        
        start = end = 0
        
        for i in range(size):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            len_tmp = max(len1, len2)
            
            if len_tmp > end - start:
                start = i - math.floor((len_tmp - 1) / 2)
                end = i + math.floor(len_tmp / 2)
        
        end += 1
        
        return s[start:end]  

    
    def expandAroundCenter(self, s:str, left, right) -> int:
        l = left
        r = right
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return r - l - 1