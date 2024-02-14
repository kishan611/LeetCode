class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        n=len(nums)
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(0,n,2):
            nums[i]=pos[i//2]
            nums[i+1]=neg[i//2]
        return nums
        
        