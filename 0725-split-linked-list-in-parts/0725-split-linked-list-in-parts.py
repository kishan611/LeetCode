# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=1
        curr=head
        if curr==None:
            return [None]*k
        while curr.next:
            curr=curr.next
            n+=1
        q,r=n//k,n%k
        res=[]
        curr=head
        for i in range(k):
            if curr:
                res.append(curr)
                for j in range(q+(i<r)-1):
                    if curr.next:
                        curr=curr.next
                n=curr.next
                curr.next=None
                curr=n
            else:
                res.append(None)
        return res