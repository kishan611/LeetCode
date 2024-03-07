# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=1
        curr=head
        if head.next==None:
            return head
        while curr.next!=None:
            n+=1
            curr=curr.next
        i=n//2
        curr=head
        while i>0:
            curr=curr.next
            i-=1
        return curr