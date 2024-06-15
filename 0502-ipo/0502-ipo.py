class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q=[]
        projects=sorted(zip(capital,profits),reverse=True)
        for i in range(k):
            while projects and projects[-1][0]<=w:
                heappush(q,-projects.pop()[1])
            if q:
                w-=heappop(q)
        return w
        