# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s={root:[]}
        root.val=0
        if root.left:
            s[root].append(root.left)
        if root.right:
            s[root].append(root.right)
        while s:
            tot=0
            curr={}
            for i,j in s.items():
                for k in j:
                    tot+=k.val
            for i,j in s.items():
                temp=tot
                for k in j:
                    temp-=k.val
                for k in j:
                    k.val=temp
            for i,j in s.items():
                for k in j:
                    curr[k]=[]
                    if k.left:
                        curr[k].append(k.left)
                    if k.right:
                        curr[k].append(k.right)
            s=curr
        return root
                    
                
        
        