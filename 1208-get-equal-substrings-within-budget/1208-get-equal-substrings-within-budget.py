class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        currcost=0
        maxl=0
        l=0
        for r in range(n):
            currcost+=abs(ord(s[r])-ord(t[r]))
            while currcost>maxCost:
                currcost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            maxl=max(maxl,r-l+1)
        return maxl
                
                
                
        