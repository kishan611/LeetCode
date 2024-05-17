import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        nodes={i for i in range(n)}
        res=0
        visited=set()
        heap=[(0,0,0)]
        while heap:
            w,s,d=heapq.heappop(heap)
            if d not in visited:
                visited.add(d)
                res+=w
                for i in nodes-visited:
                    heapq.heappush(heap,(abs(points[d][0]-points[i][0])+abs(points[d][1]-points[i][1]),d,i))
        return res
        
        
        