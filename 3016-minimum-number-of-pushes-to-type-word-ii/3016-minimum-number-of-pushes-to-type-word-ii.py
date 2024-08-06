class Solution:
    def minimumPushes(self, word: str) -> int:
        res=[0]*26
        for i in word:
            res[ord(i)-97]+=1
        res.sort(reverse=True)
        ans=sum(res[:8])+(sum(res[8:16])*2)+(sum(res[16:24])*3)+(sum(res[24:])*4)
        return ans
            
        