class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ele=max(nums)
        count=0
        max_count=0
        for i in nums:
            if i==ele:
                count+=1
                max_count=max(count,max_count)
            else:
                count=0
        return max_count