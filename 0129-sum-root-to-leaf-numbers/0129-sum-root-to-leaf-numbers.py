# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sn(self,root,ps):
        if not root:
            return 0
        ps=ps*10+root.val
        if not root.left and not root.right:
            return ps
        return self.sn(root.left,ps)+self.sn(root.right,ps)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            return self.sn(root,0)
            
            