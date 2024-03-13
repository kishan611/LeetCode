# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f=s=head
        st=[]
        ms=0
        while f and f.next:
            f=f.next.next
            st.append(s.val)
            s=s.next
        while s:
            ms=max(ms,st.pop()+s.val)
            s=s.next
        return ms
        