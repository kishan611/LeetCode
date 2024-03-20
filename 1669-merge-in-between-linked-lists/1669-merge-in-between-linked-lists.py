# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        l=1
        while l<a:
            curr=curr.next
            l+=1
        curr2=curr.next
        curr.next=list2
        while curr.next:
            curr=curr.next
        while l<b:
            curr2=curr2.next
            l+=1
        curr.next=curr2.next
        return list1
            
        