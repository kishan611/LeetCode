# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(lnk):
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
        temp=l1
        while l1.next and l2.next:
            x=l1.val+l2.val+c
            l1.val=x%10
            c=x//10
            l1=l1.next
            l2=l2.next
        x=l1.val+l2.val+c
        l1.val=x%10
        c=x//10
        if l2.next:
            l1.next=l2.next
        if c and not l1.next:
            l1.next=ListNode(c)
            l1=l1.next
        l1=l1.next
        if l1:
            while l1.next:
                x=l1.val+c
                l1.val=x%10
                c=x//10
                l1=l1.next
            x=l1.val+c
            l1.val=x%10
            c=x//10
            if c:
                l1.next=ListNode(c)
        return reverse(temp)
            
                
        