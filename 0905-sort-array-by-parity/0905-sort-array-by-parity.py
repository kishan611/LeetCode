class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            while l<r and nums[l]%2==0:
                l+=1
            while r>l and nums[r]%2!=0:
                r-=1
            nums[l],nums[r]=nums[r],nums[l]
        return nums
        