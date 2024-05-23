from collections import defaultdict
class Solution:
    def dfs(self,nums,i,k,mp):
        if i==len(nums):
            return 1
        t=0
        if mp[nums[i] - k] == 0 and mp[nums[i] + k] == 0:
            mp[nums[i]] += 1
            t = self.dfs(nums, i + 1, k, mp)
            mp[nums[i]] -= 1
        
        notTaken = self.dfs(nums, i + 1, k, mp)
        
        return t + notTaken 
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        dp=defaultdict(int)
        return self.dfs(nums,0,k,dp)-1
        