class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map={0:-1}
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            mod=curr%k
            if mod in map:
                if i-map[mod]>1:
                    return True
            else:
                map[mod]=i
        return False
        
            
        