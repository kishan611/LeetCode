class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)>4:
            a=nums[-4]-nums[0]
            for i in range(1,4):
                a=min(a,nums[-4+i]-nums[i])
            return a
        return 0





