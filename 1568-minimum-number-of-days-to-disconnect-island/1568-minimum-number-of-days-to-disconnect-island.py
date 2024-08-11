class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def number_of_island():
            visited=set()
            def dfs(i,j):
                s=[(i,j)]
                while s:
                    a,b=s.pop()
                    for i,j in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                        if 0<=i<n and 0<=j<m and grid[i][j] and (i,j) not in visited:
                            visited.add((i,j))
                            s.append((i,j))
            count=0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] and (i,j) not in visited:
                        count+=1
                        visited.add((i,j))
                        dfs(i,j)
            return count
        if number_of_island()!=1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j]=0
                    if number_of_island()!=1:
                        return 1
                    grid[i][j]=1
        return 2
                            
            
            
        