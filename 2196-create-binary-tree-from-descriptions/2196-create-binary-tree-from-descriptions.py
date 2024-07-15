# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen={}
        parent={}
        node={}
        root=-1
        for p,c,l in descriptions:
            if not seen.get(p,0):
                node[p]=TreeNode(p)
                seen[p]=1
                if not parent.get(p,0):
                    root = p
            if not seen.get(c,0):
                node[c]=TreeNode(c)
                seen[c]=1
            parent[c]=p
            if l:
                node[p].left=node[c]
            else:
                node[p].right=node[c]
        while parent.get(root,0):
            root=parent[root]
        return node[root]