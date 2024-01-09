# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1s=[]
        r2s=[]
        self.bs(root1,r1s)
        self.bs(root2,r2s)
        return r1s==r2s
    def bs(self,root,seq):
        if root is None:
            return
        if root.left is None and root.right is None:
            seq.append(str(root.val))
            return
        self.bs(root.left,seq)
        self.bs(root.right,seq)
        