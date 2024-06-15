# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculate(self,root):
        if not root:
            return 
        self.calculate(root.right)
        root.val+=self.total
        self.total=root.val
        self.calculate(root.left)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total=0
        self.calculate(root)
        return root
        