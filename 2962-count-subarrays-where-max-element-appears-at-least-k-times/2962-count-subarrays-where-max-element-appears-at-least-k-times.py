class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=[-1]
        maxe=max(nums)
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]==maxe:
                l.append(i)
                c+=1
        if c<k:
            return 0
        res=0
        for i in range(1,len(l)-k+1):
            a=l[i]-l[i-1]
            b=n-l[i+k-1]
            res+=(a*b)
        return res