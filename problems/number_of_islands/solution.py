class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = deque([(i, j)])  # Correct: Pass a list containing the tuple (i, j)
                    grid[i][j] = '0'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '0'
                    cnt += 1
        return cnt