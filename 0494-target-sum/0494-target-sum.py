class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def helper(idx,tar,cs):
            if (idx,cs) in dp:
                return dp[(idx,cs)]
            if idx<0:
                return cs==target
            pos=helper(idx-1,tar,cs+nums[idx])
            neg=helper(idx-1,tar,cs-nums[idx])
            dp[(idx,cs)]=pos+neg
            return pos+neg
        return helper(len(nums)-1,target,0)