# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr.next:
            while curr.next.val!=0:
                curr.val+=curr.next.val
                curr.next=curr.next.next
            if curr.next.next:
                curr=curr.next
            else:
                curr.next=None
        return head
        
            
        