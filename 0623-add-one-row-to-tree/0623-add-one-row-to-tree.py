# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            x=TreeNode(val,root)
            return x
        l=[root]
        cd=2
        while cd<depth:
            temp=[]
            while l:
                x=l.pop(0)
                if x:
                    temp.append(x.left)
                    temp.append(x.right)
            l=temp[::]
            cd+=1
        for i in l:
            if i:
                i.left=TreeNode(val,i.left)
                i.right=TreeNode(val,None,i.right)
        return root
        
        