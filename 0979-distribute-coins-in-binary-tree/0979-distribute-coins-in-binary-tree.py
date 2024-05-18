# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode],parent=None) -> int:
        if not root:
            return 0
        moves=self.distributeCoins(root.left,root)+self.distributeCoins(root.right,root)
        x=root.val-1
        if parent:
            parent.val+=x
        moves+=abs(x)
        return moves
        