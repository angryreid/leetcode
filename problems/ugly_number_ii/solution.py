# import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5]
        seen = {1}
        pq = [1]

        for i in range(n - 1):
            curr = heapq.heappop(pq)
            for factor in factors:
                if (next := curr * factor) not in seen:
                    seen.add(next)
                    heapq.heappush(pq, next)
        return heapq.heappop(pq)
        