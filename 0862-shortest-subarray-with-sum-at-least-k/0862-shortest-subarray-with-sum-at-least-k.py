class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q=deque()
        res=float("inf")
        cs=0
        for i in range(len(nums)):
            cs+=nums[i]
            if cs>=k:
                res=min(i+1,res)
            while q and cs-q[0][0]>=k:
                p,e=q.popleft()
                res=min(res,i-e)
            while q and q[-1][0]>cs:
                q.pop()
            q.append((cs,i))
        if res==float("inf"):
            return -1
        return res