class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        s=(n*(n+1))//2
        curr=1
        for i in range(2,n):
            curr+=i
            z=s-curr+i
            if z==curr:
                return i
        return -1