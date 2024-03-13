# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        s=[]
        while curr.next:
            if curr.val>=curr.next.val:
                s.append(curr)
            else:
                if s:
                    while s:
                        n=s.pop()
                        if n.val>=curr.next.val:
                            s.append(n)
                            n.next=curr.next
                            break
                    else:
                        head=curr.next
                else:
                    head=curr.next
            curr=curr.next
        return head                
                    
        