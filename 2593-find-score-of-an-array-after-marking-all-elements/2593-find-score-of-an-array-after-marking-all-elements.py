class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr_i=[(j,i) for i,j in enumerate(nums)]
        n=len(nums)
        arr_i.sort()
        res=0
        for i,j in arr_i:
            if nums[j]>0:
                res+=i
                if j-1>=0:
                    nums[j-1]=0
                if j+1<n:
                    nums[j+1]=0
        return res
                