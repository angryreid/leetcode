import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Get the number of rows in the grid
        m = len(moveTime)
        # Get the number of columns in the grid
        n = len(moveTime[0])
        # Define possible directions of movement (down, up, right, left)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Initialize a priority queue with the starting point (time, x, y, step)
        pq = [(0, 0, 0, 1)]  # (current_time, x, y, step)
        # Create a 2D list to track the minimum time to reach each cell
        visited = [[float('inf')] * n for _ in range(m)]
        # Set the starting point's time to 0
        visited[0][0] = 0
        
        # Process the priority queue until it's empty
        while pq:
            # Pop the cell with the smallest current time
            ct, x, y, step = heapq.heappop(pq)
            # If the destination cell is reached, return the current time
            if x == m - 1 and y == n - 1:
                return ct
            
            # Explore all possible directions from the current cell
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # Check if the new position is within the grid boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the new time to reach the new position
                    nt = max(ct, moveTime[nx][ny]) + step
                    # If the new time is less than the recorded time, update it
                    if nt < visited[nx][ny]:
                        visited[nx][ny] = nt
                        # Alternate step value for the next move
                        next_step = 2 if step == 1 else 1
                        # Push the new position and time into the priority queue
                        heapq.heappush(pq, (nt, nx, ny, next_step))
        
        # If the destination is unreachable, return -1
        return -1