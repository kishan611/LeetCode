class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset=set(wordDict)
        return self.order(s,0,wordset)
    def order(self,s,i,wordset):
        res=[]
        if i==len(s):
            res.append("")
        for j in range(i+1,len(s)+1):
            pre=s[i:j]
            if pre in wordset:
                post=self.order(s,j,wordset)
                for k in post:
                    res.append(pre+("" if k=="" else " ")+k)
        return res
            