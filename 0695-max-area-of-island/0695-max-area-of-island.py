class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxCount=0
        for i in range(m):
            for j in range(n):
                count=0
                if grid[i][j]==1:
                    s=[(i,j)]
                    while s:
                        a,b=s.pop()
                        if a<0 or a>=m or b<0 or b>=n or grid[a][b]!=1:
                            continue
                        s+=[(a+1,b),(a-1,b),(a,b-1),(a,b+1)]
                        grid[a][b]="*"
                        count+=1
                maxCount=max(count,maxCount)
        return maxCount