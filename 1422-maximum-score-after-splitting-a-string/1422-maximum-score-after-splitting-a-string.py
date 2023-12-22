class Solution:
    def maxScore(self, s: str) -> int:
        ms=c0=0
        c1=s.count('1')
        for i in range(len(s)-1):
            c0+=s[i]=='0'
            c1-=s[i]=='1'
            ms=max(ms,c0+c1)
        return ms
            