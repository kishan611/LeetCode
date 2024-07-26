class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf')]*n for i in range(n)]
        for i in range(n):
            dist[i][i]=0
        for i,j,k in edges:
            dist[i][j]=k
            dist[j][i]=k
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j]>dist[i][k]+dist[k][j]:
                        dist[i][j]=dist[i][k]+dist[k][j]
        mincount=n
        pos=-1
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=mincount:
                mincount=count
                pos=i
        return pos
        
            