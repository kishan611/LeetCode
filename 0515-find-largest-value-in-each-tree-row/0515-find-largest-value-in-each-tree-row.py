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
        res=[]
        q=[root]
        while q:
            temp=[]
            ans=float("-inf")
            while q:
                x=q.pop()
                ans=max(ans,x.val)
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            res.append(ans)
            q=temp[:]
        return res
                
        