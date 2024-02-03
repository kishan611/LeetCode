class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(k+1)
        
        for i in range(n-1,-1,-1):
            currmax=0;
            j=min(n,i+k)
            for x in range(i,j):
                currmax=max(currmax,arr[x])
                dp[i%(k+1)]=max(dp[i%(k+1)],dp[(x+1)%(k+1)]+currmax*(x-i+1))
        return dp[0]