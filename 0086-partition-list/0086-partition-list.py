# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1=less=ListNode()
        temp2=great=ListNode()
        curr=head
        while curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                great.next=curr
                great=great.next
            curr=curr.next
        great.next=None
        less.next=temp2.next
        return temp1.next
                
                