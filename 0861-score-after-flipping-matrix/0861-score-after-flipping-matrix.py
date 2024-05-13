class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        res=(1<<(m-1))*n
        for i in range(1,m):
            currVal=1<<(m-1-i)
            set=0
            for j in range(n):
                if grid[j][i]==grid[j][0]:
                    set+=1
            res+=max(set,n-set)*currVal
        return res