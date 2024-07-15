# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent={}
        child=set()
        for p,c,l in descriptions:
            child.add(c)
            if p not in parent:
                parent[p]=TreeNode(p)
            p=parent[p]
            if c not in parent:
                parent[c]=TreeNode(c)
            c=parent[c]
            if l:
                p.left=c
            else:
                p.right=c
        for i,j,k in descriptions:
            if i not in child:
                return parent[i]