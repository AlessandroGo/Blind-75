import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Use a BFS Algo
        ROWS,COLS = len(grid), len(grid[0])
        visit = set()
        islands_count = 0

        if not grid:
            return 0
        
        def bfs(r,c):
            q = collections.deque() # if just pop then it will be an iterative dfs
            visit.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                # right left up down 
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for direction_row, direction_column in directions:
                    if((r + direction_row) in range(ROWS) 
                       and (c+direction_column) in range(COLS) 
                       and grid[r+direction_row][c+direction_column] == "1"
                       and (r+direction_row,c+direction_column) not in visit):
                        q.append((r+direction_row,c+direction_column))
                        visit.add((r+direction_row,c+direction_column))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                   bfs(r,c)
                   islands_count += 1
        return islands_count 
