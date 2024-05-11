import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        rat=sorted([(w/q,q) for w,q in zip(wage,quality)])
        mr=0.0
        mq=0
        heap=[]
        for i in range(k):
            mr=max(mr,rat[i][0])
            mq+=rat[i][1]
            heapq.heappush(heap,-rat[i][1])
        mw=mr*mq
        for i in range(k,len(quality)):
            mr=max(mr,rat[i][0])
            mq+=rat[i][1]+heapq.heappop(heap)
            heapq.heappush(heap,-rat[i][1])
            mw=min(mw,mr*mq)
        return mw
            
        
        