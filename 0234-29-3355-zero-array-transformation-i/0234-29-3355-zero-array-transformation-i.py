class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        temp = [0]*(n+1)
        for i,j in queries:
            temp[i]+=1
            temp[j+1]-=1
        for i in range(1,n):
            temp[i]+=temp[i-1]
        for i in range(n):
            if nums[i]>temp[i]:
                return False
        return True
        