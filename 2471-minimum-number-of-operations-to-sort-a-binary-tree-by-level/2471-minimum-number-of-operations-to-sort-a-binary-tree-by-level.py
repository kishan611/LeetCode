from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res=0
        q=deque([root])
        while q:
            temp=[]
            while q:
                x=q.popleft()
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            d={}
            t1=[]
            for i,j in enumerate(temp):
                x=j.val
                d[x]=i
                t1.append(x)
            t2=sorted(t1)
            for i in range(len(t1)):
                if t1[i]==t2[i]:
                    continue
                x=d[t2[i]]
                d[t1[i]]=x
                d[t1[x]]=i
                t1[i],t1[x]=t1[x],t1[i]
                res+=1
            q=deque(temp[:])
        return res
            