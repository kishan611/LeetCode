class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        for i in num:
            while s and k>0 and s[-1]>i:
                k-=1
                s.pop()
            s.append(i)
        for i in range(k):
            s.pop()
        s="".join(s)
        s=s.lstrip("0")
        if s:
            return s
        return '0'
                
        