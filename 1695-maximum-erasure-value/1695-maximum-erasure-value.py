class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        res=0
        currsum=0
        j=0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[j])
                currsum-=nums[j]
                j+=1
            s.add(nums[i])
            currsum+=nums[i]
            res=max(currsum,res)
        return res