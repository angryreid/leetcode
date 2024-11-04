"""
------------------------------------------------------------
In Python, the heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. By default, heapq creates a min-heap, which means that the smallest element is always at the root of the heap.

How heapq Works:
Min-Heap: The smallest element is always at the root of the heap.
Ordering: When you push elements into the heap using heapq.heappush, the elements are ordered such that the smallest element can be popped first using heapq.heappop.
Example:
In the provided code, the priority queue pq is used to store tuples of the form (ct, x, y), where ct is the current time, and (x, y) are the coordinates. The heap is ordered by ct, so the element with the smallest ct is always popped first.

In Python's heapq module, the first element of the tuple is used as the sorting key because heapq is designed to work with the natural ordering of the elements. When you push a tuple into the heap, heapq uses the first element of the tuple to determine the order of the elements in the heap.

------------------------------------------------------------
Detailed Explanation:

Min-Heap Property:

heapq maintains the heap property, which ensures that the smallest element is always at the root of the heap.
When tuples are pushed into the heap, heapq compares the first elements of the tuples to maintain this property.
Tuple Comparison:

In Python, tuples are compared lexicographically. This means that the first elements are compared first, and if they are equal, the second elements are compared, and so on.
For example, (1, 2, 3) is considered smaller than (2, 1, 3) because 1 is smaller than 2.
Using the First Element as the Key:

By using the first element of the tuple as the key, you can control the priority of the elements in the heap.
In the provided code, the first element of the tuple (ct) represents the current time, which is used to prioritize the elements in the heap.
"""

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        if not moveTime or not moveTime[0]:
            return -1  # Handle empty grid case
        
        rows = len(moveTime)  # Number of rows
        cols = len(moveTime[0])  # Number of columns
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible directions to move
        pq = [(0, 0, 0)]  # Priority queue initialized with starting point (time, x, y)
        visited = [[float('inf')] * cols for _ in range(rows)]  # Initialize visited matrix with infinity
        visited[0][0] = 0  # Starting point has 0 time

        while pq:
            current_time, x, y = heapq.heappop(pq)  # Pop the element with the smallest time
            if x == rows - 1 and y == cols - 1:  # If we reached the bottom-right corner
                return current_time  # Return the current time
            for dx, dy in directions:  # Explore all possible directions
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:  # Check if the new position is within bounds
                    new_time = max(current_time, moveTime[new_x][new_y]) + 1  # Calculate the new time
                    if new_time < visited[new_x][new_y]:  # If the new time is less than the visited time
                        visited[new_x][new_y] = new_time  # Update the visited time
                        heapq.heappush(pq, (new_time, new_x, new_y))  # Push the new position into the priority queue
        return -1  # If we cannot reach the bottom-right corner, return -1