from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        s={}
        res=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if s.get(j,0):
                s[j].append(i)
            else:
                s[j]=[i]
        for i,j in sorted(s.items()):
            for k in sorted(j,reverse=True):
                res+=[k]*i
        return res
        
        