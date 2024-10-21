
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        
        # Add all boundary cells to the min-heap
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        water_trapped = 0
        max_height = 0

        while min_heap:
            height, r, c = heapq.heappop(min_heap)
            max_height = max(max_height, height)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Calculate trapped water
                    water_trapped += max(0, max_height - heightMap[nr][nc])
                    # Push the neighbor into the heap with the updated height
                    heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))

        return water_trapped