class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums=set(nums)
        nums2={-i for i in nums}
        nums=nums&nums2
        if nums:
            return max(nums)
        return -1
            
        