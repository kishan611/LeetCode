# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=set()
        if not head:
            return None
        while head.next:
            if head in l:
                return head
            l.add(head)
            head=head.next
        return None