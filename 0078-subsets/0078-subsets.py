class Solution:
    def __init__(self):
        self.res=[]
    def sol(self,nums,i,temp,n):
        if i==n:
            self.res.append(temp.copy())
            return
        temp.append(nums[i])
        self.sol(nums,i+1,temp,n)
        temp.pop()
        self.sol(nums,i+1,temp,n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        self.sol(nums,0,[],n)
        return self.res