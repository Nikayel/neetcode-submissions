class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROW,COL = len(grid), len(grid[0])

        def DFS(row,col):
            grid[row][col] = "0"
            for rdir,cdir in directions:
                curr_r,curr_c = rdir+row, cdir+col
                if (curr_r>=0 and curr_r < ROW and 
                curr_c>= 0 and curr_c < COL and grid[curr_r][curr_c] == "1"
                ):
                    DFS(curr_r,curr_c)

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    num_islands+=1
                    DFS(row,col)
        return num_islands

        