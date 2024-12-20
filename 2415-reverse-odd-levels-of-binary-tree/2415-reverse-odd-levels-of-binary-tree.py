from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([root])
        k=1
        while q:
            temp=[]
            while q:
                x=q.popleft()
                if x.left:
                    temp.append(x.left)
                    temp.append(x.right)
            if k:
                n=len(temp)
                for i in range(n//2):
                    temp[i].val,temp[n-i-1].val=temp[n-i-1].val,temp[i].val
                k=0
            else:
                k=1
            q=deque(temp[:])
        return root
                
            
        