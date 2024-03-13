# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pos=-1
        res,st=[],[]
        while head:
            pos+=1
            res.append(0)
            while st and st[-1][1]<head.val:
                i,v=st.pop()
                res[i]=head.val
            st.append((pos,head.val))
            head=head.next
        return res