# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        res={root.val:root}
        def traversal(node,child,l):
            if not child:
                return
            traversal(child,child.left,True)
            traversal(child,child.right,False)
            if child.val in to_delete:
                if res.get(child.val):
                    del res[child.val]
                if node:
                    if l:
                        node.left=None
                    else:
                        node.right=None
                if child.left:
                    res[child.left.val]=child.left
                if child.right:
                    res[child.right.val]=child.right
        traversal(None,root,False)
        return res.values()
        
