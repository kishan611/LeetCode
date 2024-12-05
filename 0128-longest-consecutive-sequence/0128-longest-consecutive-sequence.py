class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        res=1
        for i in nums:
            curr=1
            if i-1 not in nums:
                while i+1 in nums:
                    i+=1
                    curr+=1
                res=max(res,curr)
        return res
                
                
        