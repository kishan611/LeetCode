class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                upmin,sidemin=None,None
                if i!=0:
                    upmin=grid[i][j]+grid[i-1][j]
                if j!=0:
                    sidemin=grid[i][j]+grid[i][j-1]
                if upmin and sidemin:
                    grid[i][j]=min(upmin,sidemin)
                else:
                    grid[i][j]=upmin if upmin!=None else sidemin
        return grid[-1][-1]
                    
        