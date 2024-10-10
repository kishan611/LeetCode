class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        s=[]
        for i in range(n):
            if not s or nums[s[-1]]>nums[i]:
                s.append(i)
        res=0
        for i in range(n-1,-1,-1):
            while s and nums[s[-1]]<=nums[i]:
                res=max(i-s.pop(),res)
            if not s:
                break
        return res

            
        
        