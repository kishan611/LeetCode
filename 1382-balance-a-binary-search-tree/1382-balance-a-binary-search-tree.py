# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left)+[node.val]+inorder_traversal(node.right)
        def balance_bst(sor_lis):
            if not sor_lis:
                return 
            mid=len(sor_lis)//2
            node=TreeNode(sor_lis[mid])
            node.left=balance_bst(sor_lis[:mid])
            node.right=balance_bst(sor_lis[mid+1:])
            return node
        sor_lis=inorder_traversal(root)
        return balance_bst(sor_lis)
        