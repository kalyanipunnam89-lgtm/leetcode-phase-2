class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows,cols=len(grid),len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        def dfs(r,c,pr,pc,char):
            if visited[r][c]:
                return True
            visited[r][c]=True
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if(nr,nc)==(pr,pc):
                        continue 
                    if grid[nr][nc]==char:
                        if dfs(nr,nc,r,c,char):
                            return True
            return False
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False                              

        