class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        low,high=0,nums[-1]-nums[0]
        def numberofpairs(target):
            count=l=0
            for r in range(1,n):
                while nums[r]-nums[l]>target:
                    l+=1
                count+=r-l
            return count
        while low<high:
            mid=low+(high-low)//2
            if numberofpairs(mid)<k:
                low=mid+1
            else:
                high=mid
        return low
                