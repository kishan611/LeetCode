# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int,isLeft=True) -> Optional[TreeNode]:
        if depth==1:
            x=TreeNode(val)
            if isLeft:
                x.left=root
            else:
                x.right=root
            return x
        if not root:
            return None
        root.left=self.addOneRow(root.left,val,depth-1)
        root.right=self.addOneRow(root.right,val,depth-1,False)
        return root
        
        