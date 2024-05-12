class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def localMax(i,j):
            curr_max=0
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    curr_max=max(curr_max,grid[a][b])
            return curr_max
        n=len(grid)
        res=[[0]*(n-2) for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                res[i-1][j-1]=localMax(i,j)
        return res
        
        