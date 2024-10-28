class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d={}
        res=-1
        for i in sorted(nums):
            s=int(i**0.5)
            if s*s==i and s in d:
                d[i]=d[s]+1
                res=max(res,d[i])
            else:
                d[i]=1
        return res
        