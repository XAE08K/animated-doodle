# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxlength=0
        def maxZigZag(node,direction,length):
            if not node:
                return self.maxlength
            self.maxlength=max(self.maxlength,length)
            if direction=="left":
                maxZigZag(node.left,"right",length+1)
                maxZigZag(node.right,"left",1)
            if direction=="right":
                maxZigZag(node.right,"left",length+1)
                maxZigZag(node.left,"right",1)
            
        maxZigZag(root,"left",0)
        maxZigZag(root,"right",0)
        return self.maxlength
