class Solution:
    def minimumSteps(self, s: str) -> int:
        c1=0
        res=0
        for i in s:
            if i=='0':
                res+=c1
            else:
                c1+=1
        return res
        