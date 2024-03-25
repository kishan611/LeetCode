# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d=defaultdict(list)
        def preorder(node):
            if not node:
                return "null"
            s=",".join([str(node.val),preorder(node.left),preorder(node.right)])
            if len(d[s])==1:
                res.append(node)
            d[s].append(node)
            return s
        res=[]
        preorder(root)
        return res
                