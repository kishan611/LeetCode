# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1=even=ListNode(0)
        temp2=odd=ListNode(0)
        curr=head
        while curr and curr.next:
            even.next=curr
            odd.next=curr.next
            curr=curr.next.next
            odd=odd.next
            even=even.next
            print(odd.val,even.val)
        if curr:
            even.next=curr
            even=even.next
        odd.next=None
        even.next=temp2.next
        return temp1.next