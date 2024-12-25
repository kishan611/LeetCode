# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[root.val]
        q=[root]
        while q:
            temp=[]
            ans=float("-inf")
            while q:
                x=q.pop()
                if x.left:
                    temp.append(x.left)
                    ans=max(ans,x.left.val)
                if x.right:
                    temp.append(x.right)
                    ans=max(ans,x.right.val)
            res.append(ans)
            q=temp[:]
        res.pop()
        return res
                
        