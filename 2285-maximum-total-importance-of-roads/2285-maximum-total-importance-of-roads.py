class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        rank=[0]*n
        count=0
        for i,j in roads:
            rank[i]+=1
            rank[j]+=1
        rank.sort()
        for i in range(n):
            count+=rank[i]*(i+1)
        return count