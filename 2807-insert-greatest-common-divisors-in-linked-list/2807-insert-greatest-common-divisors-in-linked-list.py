from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr.next:
             n=ListNode(gcd(curr.val,curr.next.val))
             n.next=curr.next
             curr.next=n
             curr=n.next
        return head