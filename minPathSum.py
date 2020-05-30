class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col=len(grid[0])
        row=len(grid)
        for i in range(1,col):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,row):
            grid[j][0]+=grid[j-1][0]
        for i in range(1,row):
            for j in range(1,col):
                if i > 0 and j > 0:
                    #print(newl[i][j],'mynew')
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])

        return grid[-1][-1]
        