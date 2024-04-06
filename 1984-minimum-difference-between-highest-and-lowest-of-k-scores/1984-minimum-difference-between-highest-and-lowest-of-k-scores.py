class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minscore=nums[-1]
        for i in range(len(nums)-k+1):
            minscore=min(minscore,nums[i+k-1]-nums[i])
        return minscore