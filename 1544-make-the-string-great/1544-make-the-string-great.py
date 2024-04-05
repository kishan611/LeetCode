class Solution:
    def makeGood(self, s: str) -> str:
        s=list(s)
        n=len(s)
        i=0
        while i<n-1:
            if abs(ord(s[i])-ord(s[i+1]))==32:
                s.pop(i)
                s.pop(i)
                if i>0:
                    i-=1
                n-=2
            else:
                i+=1
        return "".join(s)
        