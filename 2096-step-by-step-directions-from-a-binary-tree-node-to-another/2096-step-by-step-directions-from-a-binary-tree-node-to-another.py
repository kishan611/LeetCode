# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start=[]
        dest=[]
        def dfs(node,val,s):
            if node.val==val:
                return True
            if node.left and dfs(node.left,val,s):
                s+="L"
            elif node.right and dfs(node.right,val,s):
                s+="R"
            return s
        dfs(root,startValue,start)
        dfs(root,destValue,dest)
        n,m=len(start),len(dest)
        while m and n and start[-1]==dest[-1]:
            start.pop()
            dest.pop()
            m-=1
            n-=1
        return "".join("U"*n)+"".join(reversed(dest))