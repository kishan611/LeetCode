# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        s=head
        f=head
        d=head
        while f and f.next:
            d=s
            s=s.next
            f=f.next.next
        root=TreeNode(s.val)
        d.next=None
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(s.next)
        return root