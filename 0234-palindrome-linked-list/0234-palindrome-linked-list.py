# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=f=head
        rev=None
        while f and f.next:
            f=f.next.next
            rev,rev.next,s=s,rev,s.next
            
        if f:
            s=s.next
        while s:
            if s.val!=rev.val:
                return False
            s=s.next
            rev=rev.next
        else:
            return True
        