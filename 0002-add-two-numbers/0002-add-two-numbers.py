# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        temp=l1
        while l1.next and l2.next:
            x=l1.val+l2.val+carry
            l1.val=x%10
            carry=x//10
            l1=l1.next
            l2=l2.next
        x=l1.val+l2.val+carry
        l1.val=x%10
        carry=x//10
        l2=l2.next
        while l1.next:
            l1=l1.next
            x=l1.val+carry
            l1.val=x%10
            carry=x//10
        else:
            if carry and not l2:
                l1.next=ListNode(carry)
                l1=l1.next
                l1=l1.next
        if l1:
            l1.next=l2
            while l1.next:
                l1=l1.next
                print(carry)
                x=l1.val+carry
                l1.val=x%10
                carry=x//10
            else:
                if carry:
                    l1.next=ListNode(carry)
                
        return temp
            
            
            
