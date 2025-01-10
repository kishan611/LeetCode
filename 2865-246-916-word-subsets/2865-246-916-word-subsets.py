from collections import defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res=[]
        d={}
        for i in words2:
            dd={}
            for j in i:
                dd[j]=dd.get(j,0)+1
                d[j]=max(d.get(j,0),dd[j])
        for i in words1:
            d1={}
            for j in i:
                d1[j]=d1.get(j,0)+1
            for a,b in d.items():
                if d1.get(a,0)<b:
                    break
            else:
                res.append(i)
        return res

        