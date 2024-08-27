class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist=[0]*n
        dist[start_node]=1
        for i in range(n-1):
            flag=0
            for idx,(u,v) in enumerate(edges):
                if dist[u]*succProb[idx]>dist[v]:
                    dist[v]=dist[u]*succProb[idx]
                    flag=1
                if dist[v]*succProb[idx]>dist[u]:
                    dist[u]=dist[v]*succProb[idx]
                    flag=1
            if not flag:
                break
        return dist[end_node]