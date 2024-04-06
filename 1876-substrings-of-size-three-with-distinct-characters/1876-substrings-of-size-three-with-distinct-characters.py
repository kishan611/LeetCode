class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)-2):
            a=s[i]
            b=s[i+1]
            c=s[i+2]
            if a==b or a==c or b==c:
                continue
            else:
                res+=1
        return res