class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        if n<k:
            return 0
        res=0
        dp=[1]*(2*n)
        colors=colors+colors
        for i in range(1,2*n):
            if colors[i]!=colors[i-1]:
                dp[i]=1+dp[i-1]
        for i in range(n):
            if dp[i]>=k or dp[i+n]>=k:
                res+=1
        return res

