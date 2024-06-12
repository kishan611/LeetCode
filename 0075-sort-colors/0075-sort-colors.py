class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=Counter(nums)
        z=a.get(0,0)
        o=a.get(1,0)
        t=a.get(2,0)
        for i in range(z):
            nums[i]=0
        for i in range(z,z+o):
            nums[i]=1
        for i in range(z+o,z+o+t):
            nums[i]=2
        