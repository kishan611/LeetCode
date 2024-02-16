class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(),key= lambda item:item[1]))
        b=1
        count=0
        ans=0
        for i ,j in d.items():
            if b and count+j<=k:
                count+=j
            else:
                b=0
                ans+=1
        return ans