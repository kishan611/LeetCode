import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap=[]
        n=len(arr)
        for i in range(n-1):
            heapq.heappush(heap,(arr[i]/arr[-1],i,n-1))
        for i in range(k-1):
            rem,num,den=heapq.heappop(heap)
            if den-1>num:
                heapq.heappush(heap,(arr[num]/arr[den-1],num,den-1))
        rem,num,den=heapq.heappop(heap)
        return [arr[num],arr[den]]