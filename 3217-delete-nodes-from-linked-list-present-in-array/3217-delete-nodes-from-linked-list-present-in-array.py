# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=curr=ListNode(0,head)
        nums=set(nums)
        while curr.next:
            if curr.next.val in nums:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
        