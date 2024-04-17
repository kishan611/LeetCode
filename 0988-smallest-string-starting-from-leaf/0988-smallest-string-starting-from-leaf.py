# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root,path,smallest):
            if not root:
                return None
            path.append(chr(root.val+97))
            if not root.left and not root.right:
                x="".join(path)[::-1]
                smallest[0]=min(smallest[0],x)
            dfs(root.left,path,smallest)
            dfs(root.right,path,smallest)
            path.pop()
        smallest=[chr(123)]
        path=[]
        dfs(root,path,smallest)
        return smallest[0]