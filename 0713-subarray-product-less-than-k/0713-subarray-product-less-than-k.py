class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        start=end=0
        count=0
        curr=1
        while end<len(nums):
            curr*=nums[end]
            while curr>=k:
                curr//=nums[start]
                start+=1
            count+=(end-start)+1
            end+=1
        return count
            