class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(),key= lambda item:item[1]))
        ans=len(d)
        for i ,j in d.items():
            if j<=k:
                k-=j
                ans-=1
            else:
                break
        return ans