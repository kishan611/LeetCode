class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        for i in range(n,0,-1):
            if nums[n-i]>=i:
                if n-i!=0:
                    if nums[n-i-1]<i:
                        return i
                else:
                    return i
        return -1
        