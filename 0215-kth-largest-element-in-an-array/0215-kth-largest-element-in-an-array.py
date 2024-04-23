import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in nums[k::]:
            heapq.heappush(heap,i)
            heapq.heappop(heap)
        return heap[0]
        