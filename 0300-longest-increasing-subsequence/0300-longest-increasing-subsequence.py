class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        def fun(i):
            if i in memo:
                return memo[i]
            length=1
            for j in range(i):
                if nums[i]>nums[j]:
                    length=max(length,fun(j)+1)
            memo[i]=length
            return length
        max_len=0
        for i in range(len(nums)):
            max_len=max(max_len,fun(i))
        return max_len
        