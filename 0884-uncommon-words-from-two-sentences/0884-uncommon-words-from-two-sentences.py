class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        for i in s1.split()+s2.split():
            d[i]=d.get(i,0)+1
        res=[]
        for i,j in d.items():
            if j==1:
                res.append(i)
        return res
            