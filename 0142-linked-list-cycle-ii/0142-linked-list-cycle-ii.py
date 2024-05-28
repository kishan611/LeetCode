# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=set()
        s=f=head
        while f and f.next:
            if f in l:
                return f
            if f.next in l:
                return f.next
            
            l.add(s)
            s=s.next
            f=f.next.next
        return None
            
        