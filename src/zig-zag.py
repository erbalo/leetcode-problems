"""
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        pl = 1
        outp = [""] * numRows
        
        for i in range(len(s)):            
            outp[lin] += s[i]
            
            if numRows > 1:
                lin += pl
                
                if lin == 0 or lin == numRows - 1:
                    pl *= -1
        # New comment

        output = ""
        
        for j in range(numRows):
            output += outp[j]
            
        return output
