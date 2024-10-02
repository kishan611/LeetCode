class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        for i,j in enumerate(sorted(set(arr))):
            d[j]=i
        res=[]
        for i in arr:
            res.append(d[i]+1)
        return res
        