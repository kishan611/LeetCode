class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k=sum(nums)
        n=len(nums)
        m=curr=sum(nums[:k])
        for i in range(k,n+k):
            curr+=nums[i%n]
            curr-=nums[(i-k)%n]
            m=max(m,curr)
        return k-m
        