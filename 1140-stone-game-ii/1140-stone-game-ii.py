class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp=[[0]*(n+1) for _ in range(n)]
        ss=[0]*n
        ss[-1]=piles[-1]
        for i in range(n-2,-1,-1):
            ss[i]=ss[i+1]+piles[i]
        for i in range(n-1,-1,-1):
            for m in range(1,n+1):
                if i+2*m>=n:
                    dp[i][m]=ss[i]
                else:
                    for x in range(1,2*m+1):
                        dp[i][m]=max(dp[i][m],ss[i]-dp[i+x][max(m,x)])
        return dp[0][1]

        