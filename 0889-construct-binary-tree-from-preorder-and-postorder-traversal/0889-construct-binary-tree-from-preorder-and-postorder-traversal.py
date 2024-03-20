# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None
        if len(postorder)==1:
            return TreeNode(postorder[0])
        root=TreeNode(preorder[0])
        left=preorder[1]
        left_s=postorder.index(left)+1
        root.left=self.constructFromPrePost(preorder[1:left_s+1],postorder[:left_s])
        root.right=self.constructFromPrePost(preorder[left_s+1:],postorder[left_s:-1])
        return root
        