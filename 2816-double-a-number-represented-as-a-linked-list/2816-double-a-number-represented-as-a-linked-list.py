# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(num):
            prev=None
            curr=num
            while curr:
                x=curr.next
                curr.next=prev
                prev=curr
                curr=x
            return prev
        head=reverse(head)
        curr=head
        carry=0
        while curr.next:
            x=curr.val*2+carry
            curr.val=x%10
            carry=x//10
            curr=curr.next
        x=curr.val*2+carry
        curr.val=x%10
        carry=x//10
        if carry:
            curr.next=ListNode(carry)
        return reverse(head)