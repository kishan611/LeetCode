from math import log
class Solution:
    def numSquares(self, n: int) -> int:
        if n<=3:
            return n
        s=[i*i for i in range(1,int(n**0.5)+1)]
        if n in s:
            return 1
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in s:
            for j in range(i,n+1):
                dp[j] = min(dp[j], dp[j -i ] + 1)
        return dp[n]
        '''x=int(n**0.5)
        ps=[i**2 for i in range(x,0,-1)]
        i=0
        res=0
        while i+1<x:
            if ps[i]>n:
                i+=1
                continue
            if n%ps[i]==0:
                res+=n//ps[i]
                n=0
            if n%ps[i] in ps:
                res+=n//ps[i]+1
                n=0
            if n%ps[i]>n%ps[i+1] and ps[i+1]!=1:
                i+=1
            elif n%ps[i]<n%ps[i+1]:
                res+=n//ps[i]
                n-=ps[i]*res
                i+=1
            else:
                res=n//ps[i]
                res+=n-ps[i]*res
                n=0
                i+=1
            
            print(i)
        if n>0:
            res+=n
        return res'''
        