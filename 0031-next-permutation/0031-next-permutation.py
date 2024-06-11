class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        def reverse(start):
            end=n-1
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        i1=i2=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                i1=i
                break
        if i1==-1:
            reverse(0)
        else:
            for i in range(n-1,-1,-1):
                if nums[i]>nums[i1]:
                    i2=i
                    break
            swap(i1,i2)
            reverse(i1+1)
        