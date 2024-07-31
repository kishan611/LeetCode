class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            tw=mh=0
            for j in range(i,0,-1):
                tw+=books[j-1][0]
                if tw>shelfWidth:
                    break
                mh=max(mh,books[j-1][1])
                dp[i]=min(dp[i],dp[j-1]+mh)
        return dp[n]
        