class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z=0
        res=1
        for i in nums:
            if i==0:
                z+=1
            else:
                res*=i
        n=len(nums)
        if z>1:
            return [0]*n
        if z==1:
            i=nums.index(0)
            nums=[0]*n
            nums[i]=res
            return nums
            return nums
        for i in range(n):
            nums[i]=res//nums[i]
        return nums