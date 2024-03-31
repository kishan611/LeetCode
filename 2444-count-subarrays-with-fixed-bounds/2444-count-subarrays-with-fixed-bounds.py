class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        maxi,mini=-1,-1
        l=0
        ans=0
        for r in range(len(nums)):
            x=nums[r]
            if x>maxK or x<minK:
                l=r+1
                continue
            if x==minK:
                mini=r
            if x==maxK:
                maxi=r
            ans+=max((min(mini,maxi)-l+1),0)
        return ans
            
                