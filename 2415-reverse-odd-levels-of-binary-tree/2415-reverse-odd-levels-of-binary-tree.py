from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        def travel(left,right,level):
            if not left or not right:
                return 
            if level%2!=0:
                left.val,right.val=right.val,left.val
            travel(left.left,right.right,level+1)
            travel(left.right,right.left,level+1)
        travel(root.left,root.right,1)
        return root