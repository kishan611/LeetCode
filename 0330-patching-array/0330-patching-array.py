class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i,m,res=0,1,0
        while m<=n:
            if i<len(nums) and nums[i]<=m:
                m+=nums[i]
                i+=1
            else:
                m+=m
                res+=1
        return res
        