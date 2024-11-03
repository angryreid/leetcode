import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(0, 0, 0)]
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0
        while pq:
            ct, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return ct
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nt = max(ct, moveTime[nx][ny]) + 1
                    if nt < visited[nx][ny]:
                        visited[nx][ny] = nt
                        heapq.heappush(pq, (nt, nx, ny))
        return -1
        