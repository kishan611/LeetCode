class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={i:0 for i in range(n)}
        for i,j in roads:
            d[i]+=1
            d[j]+=1
        rank=[0]*n
        x=1
        for i,j in sorted(d.items(),key=lambda x:x[1]):
            rank[i]=x
            x+=1
        res=0
        for i,j in roads:
            res+=rank[i]+rank[j]
        return res