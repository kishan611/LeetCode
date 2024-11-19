class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k==1:
            return max(nums)
        i=res=curr=0
        n=len(nums)
        temp=set()
        for j in range(n):
            if nums[j] not in temp:
                curr+=nums[j]
                temp.add(nums[j])
                if j-i+1==k:
                    res=max(curr,res)
                    curr-=nums[i]
                    temp.remove(nums[i])
                    i+=1
            else:
                while nums[i]!=nums[j]:
                    curr-=nums[i]
                    temp.remove(nums[i])
                    i+=1
                i+=1
        return res
        
        