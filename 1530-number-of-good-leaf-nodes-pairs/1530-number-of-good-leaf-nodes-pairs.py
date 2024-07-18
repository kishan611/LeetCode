# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        d={}
        leaves=[]
        def findleaf(node,trail):
            if not node:
                return 
            temp=trail[::]
            temp.append(node)
            if not node.left and not node.right:
                d[node]=temp
                leaves.append(node)
                return 
            findleaf(node.left,temp)
            findleaf(node.right,temp)
        res=0
        findleaf(root,[])
        for i in range(len(leaves)):
            for j in range(i+1,len(leaves)):
                li=d.get(leaves[i],None)
                lj=d.get(leaves[j],None)
                n,m=len(li),len(lj)
                for k in range(min(n,m)):
                    if li[k]!=lj[k]:
                        curr=m+n-2*k
                        if curr<=distance:
                            res+=1
                        break
        return res
        