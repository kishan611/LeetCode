class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float("inf")
        n=len(nums)
        for i in range(len(nums)-2):
            j,k=i+1,n-1
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if abs(x-target)<abs(ans-target):
                    ans=x
                if x<target:
                    j+=1
                elif x>target:
                    k-=1
                else:
                    return x
        return ans

