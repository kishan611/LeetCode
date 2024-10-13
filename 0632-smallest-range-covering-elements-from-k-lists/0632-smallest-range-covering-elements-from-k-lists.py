import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h=[]
        mx=float("-inf")
        for i in range(len(nums)):
            heapq.heappush(h,(nums[i][0],i,0))
            mx=max(mx,nums[i][0])
        res=[float("-inf"),float("inf")]
        while h:
            ele,li,i=heapq.heappop(h)
            if mx-ele<res[1]-res[0]:
                res=[ele,mx]
            if i+1<len(nums[li]):
                nxt=nums[li][i+1]
                heapq.heappush(h,(nxt,li,i+1))
                mx=max(mx,nxt)
            else:
                break
        return res