class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr=max_global=nums[0]
        for i in nums[1:]:
            max_curr=max(i,max_curr+i)
            max_global=max(max_global,max_curr)
        return max_global
        