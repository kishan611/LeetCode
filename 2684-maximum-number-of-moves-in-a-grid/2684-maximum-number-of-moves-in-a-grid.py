class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            total_sum = 0
            for j in range(len(grid)):
                if not j:
                    if grid[j][i-1] >= grid[j][i] and grid[j+1][i-1] >= grid[j][i]:
                        grid[j][i] = 2000000
                elif j == len(grid) - 1:
                    if grid[j][i-1] >= grid[j][i] and grid[j-1][i-1] >= grid[j][i]:
                        grid[j][i] = 2000000
                else:
                    if grid[j][i-1] >= grid[j][i] and grid[j-1][i-1] >= grid[j][i] and grid[j+1][i-1] >= grid[j][i]:
                        grid[j][i] = 2000000
                total_sum += grid[j][i]
            if total_sum / len(grid) == 2000000:
                return i -1
        return i