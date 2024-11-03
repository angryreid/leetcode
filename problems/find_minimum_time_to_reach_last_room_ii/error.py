import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(0, 0, 0, 1)]
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0
        
        while pq:
            ct, x, y, step = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return ct
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nt = max(ct, moveTime[nx][ny]) + step
                    if nt < visited[nx][ny]:
                        step = 2 if step == 1 else 1 # This is the error, return a new step
                        visited[nx][ny] = nt
                        heapq.heappush(pq, (nt, nx, ny, step))
        return -1