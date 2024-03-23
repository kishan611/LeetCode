# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        x=s.next
        s.next=None
        prev=None
        curr=x
        while curr:
            x=curr.next
            curr.next=prev
            prev=curr
            curr=x
        curr=head
        while curr and prev:
            x=curr.next
            curr.next=prev
            prev=prev.next
            curr.next.next=x
            curr=curr.next.next
        
        