import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[]
        for i in gifts:
            heapq.heappush(h,-i)
        for i in range(k):
            x=int(abs(heapq.heappop(h))**0.5)
            heapq.heappush(h,-x)
        res=0
        while h:
            res+=abs(heapq.heappop(h))
        return res
        