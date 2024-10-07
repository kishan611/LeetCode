class Solution:
    def minLength(self, s: str) -> int:
        res=[]
        for i in s:
            if res and ((i=="B" and res[-1]=='A') or(i=="D" and res[-1]=="C")) :
                res.pop()
            else:
                res.append(i)
        return len(res)