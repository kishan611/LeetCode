class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid1[0] or not grid2 or not grid2[0]:
            return 0

        m, n = len(grid1), len(grid1[0])
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs_explore(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid2[r][c] == 0:
                return True 
            
            grid2[r][c] = 0

            if grid1[r][c] == 0:
                nonlocal is_sub_island 
                is_sub_island = False

            for dr, dc in dire:
                dfs_explore(r + dr, c + dc)
            
            return is_sub_island

        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    is_sub_island = True 
                    if dfs_explore(row, col):
                        res += 1

        return res