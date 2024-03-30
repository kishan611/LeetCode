class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarray(nums,k)-self.subarray(nums,k-1)
    def subarray(self,nums,k):
        d={}
        l=r=0
        c=0
        res=0
        while r<len(nums):
            if d.get(nums[r],0):
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
                c+=1
            while c>k:
                if d[nums[l]]-1==0:
                    c-=1
                d[nums[l]]-=1
                l+=1
            res+=r-l+1
            r+=1
        return res