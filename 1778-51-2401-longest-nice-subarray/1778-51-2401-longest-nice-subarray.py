class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        temp = 0
        i = 0
        res = 0
        for j,v in enumerate(nums):
            while temp&v:
                temp^=nums[i]
                i+=1
            res = max(res,j-i+1)
            temp|=v
        return res

