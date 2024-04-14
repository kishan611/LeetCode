# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def sub(self,root):
        if not root:
            return 
        if root.left:
            if not root.left.left and not root.left.right:
                self.res+=root.left.val
        self.sub(root.left)
        self.sub(root.right)
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sub(root)
        return self.res