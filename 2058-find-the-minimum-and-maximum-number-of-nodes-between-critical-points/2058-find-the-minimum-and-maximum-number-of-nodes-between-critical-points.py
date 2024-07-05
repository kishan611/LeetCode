# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        mind=float("inf")
        count=1
        f=prevc=0
        while curr and curr.next:
            count+=1
            if prev.val<curr.val>curr.next.val or prev.val>curr.val<curr.next.val:
                if not f:
                    f=count
                    prevc=f
                else:
                    mind=min(mind,count-prevc)
                    prevc=count
            prev=curr
            curr=curr.next
        if mind!=float("inf"):
            return [mind,prevc-f]
        return [-1,-1]
                
        