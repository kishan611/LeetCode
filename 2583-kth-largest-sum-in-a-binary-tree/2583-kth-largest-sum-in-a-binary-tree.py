# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        s=[root]
        while s:
            temp=[]
            tot=0
            while s:
                x=s.pop()
                tot+=x.val
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            s=temp[::]
            res.append(tot)
        if len(res)<k:
            return -1
        return sorted(res,reverse=True)[k-1]
        
        
        