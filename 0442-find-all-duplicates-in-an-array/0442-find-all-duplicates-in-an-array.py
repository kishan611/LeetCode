class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            x=abs(nums[i])
            if nums[x-1]>0:
                nums[x-1]=-nums[x-1]
            else:
                res.append(x)
        return res
            