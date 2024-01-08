class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a=1
        b=2
        res=2
        for i in range(3,n+1):
            res=a+b
            a=b
            b=res
        return res