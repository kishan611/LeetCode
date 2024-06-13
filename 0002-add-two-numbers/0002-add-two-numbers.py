# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        temp=dummy
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=x+y+carry
            temp.next=ListNode(s%10)
            carry=s//10
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
            
            
            
