import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(0, 0, 0, 1)]  # (current_time, x, y, step)
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0
        
        while pq:
            ct, x, y, step = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return ct
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the new time to reach (nx, ny)
                    nt = max(ct, moveTime[nx][ny]) + step
                    if nt < visited[nx][ny]:
                        visited[nx][ny] = nt
                        # Alternate step value for the next move
                        next_step = 2 if step == 1 else 1
                        heapq.heappush(pq, (nt, nx, ny, next_step))
        
        return -1  # If the destination is unreachable
