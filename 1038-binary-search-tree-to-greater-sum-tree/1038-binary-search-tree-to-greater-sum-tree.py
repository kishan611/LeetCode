# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr=root
        val=0
        s=[]
        while curr or s:
            while curr:
                s.append(curr)
                curr=curr.right
            curr=s.pop()
            val+=curr.val
            curr.val=val
            curr=curr.left
        return root
                
        