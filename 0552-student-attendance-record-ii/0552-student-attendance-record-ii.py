class Solution:
    def checkRecord(self, n: int) -> int:
        mod=10**9+7
        dp=[[1]*3 for _ in range(2)]
        for p in range(1,n+1):
            ndp=[[0]*3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    ndp[a][l]+=dp[a][2]
                    ndp[a][l]%=mod
                    if a>0:
                        ndp[a][l]+=dp[a-1][2]
                        ndp[a][l]%=mod
                    if l>0:
                        ndp[a][l]+=dp[a][l-1]
                        ndp[a][l]%=mod
            dp=ndp
        return dp[1][2]
    