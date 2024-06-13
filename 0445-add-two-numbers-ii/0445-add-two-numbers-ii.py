# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(lnk):
            if not lnk or not lnk.next:
                return lnk
            prev=None
            temp=lnk
            while temp:
                x=temp.next
                temp.next=prev
                prev=temp
                temp=x
            return prev
        l1=reverse(l1)
        l2=reverse(l2)
        c=0
        dummy=ListNode()
        temp=dummy
        while l1 or l2 or c:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=x+y+c
            temp.next=ListNode(s%10)
            c=s//10
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return reverse(dummy.next)
        