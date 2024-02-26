# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val==q.val:
                a=self.isSameTree(p.left,q.left)
                b=self.isSameTree(p.right,q.right)
                if a and b:
                    return True
                return False
            else:
                return False
        if p and (not q):
            return False
        if (not p) and q:
            return False
        else:
            return True
        