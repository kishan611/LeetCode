class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        peri=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    peri+=4
                    if j-1>=0:
                        peri-=grid[i][j-1]
                    if j+1<n:
                        peri-=grid[i][j+1]
                    if i-1>=0:
                        peri-=grid[i-1][j]
                    if i+1<m:
                        peri-=grid[i+1][j]
        return peri
                
        