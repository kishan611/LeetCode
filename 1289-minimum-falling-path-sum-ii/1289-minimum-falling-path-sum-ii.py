class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n-2,-1,-1):
            min1=min2=20000
            for j in grid[i+1]:
                if min1>j:
                    min2=min1
                    min1=j
                elif j<min2:
                    min2=j
            for j in range(n):
                if grid[i+1][j]==min1:
                    grid[i][j]+=min2
                else:
                    grid[i][j]+=min1
        return min(grid[0])