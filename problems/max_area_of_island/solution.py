class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        cnt = 0
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            else:
                return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 grid[i][j] = 0
    #                 cnt = 1
    #                 q = deque([(i, j)])
    #                 while q:
    #                     x, y = q.popleft()
    #                     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #                         nx, ny = x + dx, y + dy
    #                         if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
    #                             grid[nx][ny] = 0
    #                             q.append((nx, ny))
    #                             cnt += 1
    #                 res = max(res, cnt)
    #     return res