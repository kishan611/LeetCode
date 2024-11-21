class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for i in range(m)]
        for i in walls+guards:
            grid[i[0]][i[1]]=1
        for i in guards:
            x,y=i[0],i[1]
            a=x-1
            while a>=0 and grid[a][y]!=1:
                grid[a][y]=2
                a-=1
            a=x+1
            while a<m and grid[a][y]!=1:
                grid[a][y]=2
                a+=1
            b=y-1
            while b>=0 and grid[x][b]!=1:
                grid[x][b]=2
                b-=1
            b=y+1
            while b<n and grid[x][b]!=1:
                grid[x][b]=2
                b+=1
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    count+=1
        return count