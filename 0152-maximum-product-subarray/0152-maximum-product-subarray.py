class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s=e=1
        res=float("-inf")
        n=len(nums)
        for i in range(n):
            s*=nums[i]
            e*=nums[n-i-1]
            res=max(res,max(s,e))
            if s==0:
                s=1
            if e==0:
                e=1
        return res
        