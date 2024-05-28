class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        cost=[abs(ord(s[i])-ord(t[i])) for i in range(n)]
        curr=0
        currlength=0
        maxl=0
        l=r=0
        while l<n and r<n:
            if curr+cost[r]<=maxCost:
                curr+=cost[r]
                currlength+=1
                r+=1
                maxl=max(maxl,currlength)
            else:
                curr-=cost[l]
                currlength-=1
                l+=1
        return maxl
                
                
                
        