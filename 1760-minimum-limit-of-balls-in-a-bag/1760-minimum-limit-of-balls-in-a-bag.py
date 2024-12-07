class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r=1,max(nums)
        while l<r:
            m=(l+r)//2
            if sum((i-1)//m for i in nums)<=maxOperations:
                r=m
            else:
                l=m+1
        return r