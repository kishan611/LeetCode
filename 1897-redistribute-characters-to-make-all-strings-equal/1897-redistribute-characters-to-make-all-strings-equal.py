class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        x=len(words)
        for i in d.values():
            if i%x!=0:
                return False
        return True
        