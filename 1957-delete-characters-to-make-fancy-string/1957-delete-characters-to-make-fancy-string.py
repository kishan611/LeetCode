class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[0]
        c=1
        for i in range(1,len(s)):
            if s[i]==s[i-1] and c<2:
                res+=s[i]
                c+=1
            elif s[i-1]!=s[i]:
                res+=s[i]
                c=1
        return res
        