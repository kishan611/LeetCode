import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h=[(j,i) for i,j in enumerate(nums)]
        heapq.heapify(h)
        for i in range(k):
            x=heapq.heappop(h)
            nums[x[1]]*=multiplier
            heapq.heappush(h,(nums[x[1]],x[1]))
        return nums