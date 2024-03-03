# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=1
        curr=head
        while curr.next!=None:
            curr=curr.next
            l+=1
        n=l-n+1
        if n==1:
            head=head.next
            return head
        curr=head
        while n>2:
            curr=curr.next
            n-=1
        curr.next=curr.next.next
        return head
            
        