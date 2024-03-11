class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        res=""
        for i in order:
            d[i]=0
        for i in s:
            if d.get(i,-1)!=-1:
                d[i]+=1
            else:
                res+=i
        for i,j in d.items():
            res+=i*j
        return res
        