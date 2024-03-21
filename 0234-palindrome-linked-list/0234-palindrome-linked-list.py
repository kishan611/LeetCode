# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        prev=None
        while s.next:
            x=s.next
            s.next=prev
            prev=s
            s=x
        s.next=prev
        while s:
            if s.val!=head.val:
                return False
            s=s.next
            head=head.next
        else:
            return True
        