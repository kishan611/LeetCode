class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=res=0
        for i in s:
            if i=="(":
                o+=1
            elif o>0:
                o-=1
            else:
                res+=1
        return res+o
        