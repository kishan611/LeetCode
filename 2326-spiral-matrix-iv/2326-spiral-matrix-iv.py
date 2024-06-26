# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res=[[0 for _ in range(n)] for i in range(m)]
        t,b,l,r=0,m-1,0,n-1
        x=head
        while t<=b and l<=r:
            for i in range(l,r+1):
                if x:
                    res[t][i]=x.val
                    x=x.next
                else:
                    res[t][i]=-1
            t+=1
            for i in range(t,b+1):
                if x:
                    res[i][r]=x.val
                    x=x.next
                else:
                    res[i][r]=-1
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    if x:
                        res[b][i]=x.val
                        x=x.next
                    else:
                        res[b][i]=-1
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    if x:
                        res[i][l]=x.val
                        x=x.next
                    else:
                        res[i][l]=-1
                l+=1
        return res
        