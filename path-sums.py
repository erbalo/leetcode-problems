"""
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
Expected 3

[10,5,-3,3,2,null,11,3,-2,null,1]
8
Expected 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0
        self.k = 0
        self.h = {}
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:        
        self.k = targetSum
        self.preorder(root, 0)
        
        return self.count
    
    
    def preorder(self, node: TreeNode, curr_sum):
        if node == None:
            return
        
        curr_sum += node.val
        
        if curr_sum == self.k:
            self.count += 1
        
        if curr_sum - self.k in self.h:
            self.count += self.h[curr_sum - self.k]        
        
        if curr_sum in self.h:
           self.h[curr_sum] = self.h[curr_sum] + 1
        else:
            self.h[curr_sum] = 1
        
        self.preorder(node.left, curr_sum)
        self.preorder(node.right, curr_sum)
        
        self.h[curr_sum] = self.h[curr_sum] - 1
    