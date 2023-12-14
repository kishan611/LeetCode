class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        onesRow=[]
        onesCol=[]
        for i in grid:
            onesRow.append(i.count(1))
        for i in range(n):
            c=0
            for j in range(m):
                if grid[j][i]==1:
                    c+=1
            onesCol.append(c)
        diff=[]
        for i in range(m):
            x=[]
            for j in range(n):
                x.append(2*onesRow[i]+2*onesCol[j]-m-n)
            diff.append(x)
        return diff
                
                
            
        