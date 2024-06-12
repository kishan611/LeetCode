class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s,m,e=0,0,len(nums)-1
        while m<=e:
            if nums[m]==0:
                nums[s],nums[m]=nums[m],nums[s]
                s+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[e],nums[m]=nums[m],nums[e]
                e-=1