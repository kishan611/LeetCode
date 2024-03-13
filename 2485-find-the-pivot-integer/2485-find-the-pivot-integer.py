class Solution:
    def pivotInteger(self, n: int) -> int:
        if (x:=((n*(n+1))//2)**0.5)%1==0:
            return int(x)
        return -1