class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=[0]*(n+1)
        count[0]=1
        res=0
        temp=0
        for i in nums:
            temp+=i&1
            if temp-k>=0:
                res+=count[temp-k]
            count[temp]+=1
        return res