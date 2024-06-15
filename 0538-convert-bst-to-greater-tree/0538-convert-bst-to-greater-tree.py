# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        curr,val,s=root,0,[]
        while curr or s:
            while curr:
                s.append(curr)
                curr=curr.right
            curr=s.pop()
            val+=curr.val
            curr.val=val
            curr=curr.left
        return root
        