class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def gap(a,b,n):
            res=0
            while a<=n:
                res+=min(n+1,b)-a
                a*=10
                b*=10
            return res
        i=num=1
        while i<k:
            r=gap(num,num+1,n)
            if i+r<=k:
                i+=r
                num+=1
            else:
                i+=1
                num*=10
        return num