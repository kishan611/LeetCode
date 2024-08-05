class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        res=[i for i,j in d.items() if j==1]
        if len(res)>=k:
            return res[k-1]
        return ""
        