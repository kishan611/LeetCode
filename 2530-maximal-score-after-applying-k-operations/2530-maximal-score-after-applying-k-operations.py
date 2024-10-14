class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[-i for i in nums]
        heapq.heapify(h)
        res=0
        for i in range(k):
            x=-heapq.heappop(h)
            res+=x
            if x==1:
                res+=k-1-i
                break
            heapq.heappush(h,-math.ceil(x/3))
        return res