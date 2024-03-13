# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n=1
        curr=head
        while curr.next:
            curr=curr.next
            n+=1
        s=[]
        x=n//2
        curr=head
        while n>x:
            s.append(curr)
            n-=1
            curr=curr.next
        x=0
        while curr.next:
            x=max(curr.val+s.pop().val,x)
            curr=curr.next
        x=max(curr.val+s.pop().val,x)
        return x
        