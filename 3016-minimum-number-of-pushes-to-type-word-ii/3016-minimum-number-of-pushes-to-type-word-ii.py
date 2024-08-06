class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            d[i]=d.get(i,0)+1
        res=list(d.values())
        res.sort(reverse=True)
        ans=sum(res[:8])+(sum(res[8:16])*2)+(sum(res[16:24])*3)+(sum(res[24:])*4)
        return ans
            
        