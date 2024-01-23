class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=nums[0]
        for i in nums[1::]:
            s=s^i
        return s
            