class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        arr=[0]*n
        for i in range(1,n):
            arr[i]=arr[i-1]
            if (nums[i]%2==0 and nums[i-1]%2==0) or (nums[i]%2!=0 and nums[i-1]%2!=0):
                arr[i]+=1
        ans=[]
        for i,j in queries:
            temp = arr[j]-arr[i]
            ans.append(temp==0)
        return ans