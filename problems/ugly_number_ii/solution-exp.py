class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # For any given ugly number, multiplying it by 2, 3, or 5 will yield 3 ugly numbers
        # Therefore, for each ugly number, multiply it by 2, 3, and 5, and sort the results
        # Hence, 2, 3, and 5 are the prime factors we need to handle
        factors = [2, 3, 5]

        # Since multiplying some ugly numbers by 2, 3, or 5 can result in duplicate elements
        # For example, multiplying ugly number 2 by 2, 3, and 5 yields 4, [6], 10
        # And multiplying ugly number 3 by 2, 3, and 5 yields [6], 9, 15
        # Where [6] is duplicated, so we need to remove duplicates
        # Given that n can be as large as 1690, the range of ugly numbers can exceed the int range, so we use long to store them

        # Use a priority queue to get the smallest number from the set each time
        seen = {1}  # The first number in the set is 1

        # Elements in the priority queue come from the seen set
        pq = [1]

        # Start iterating over the values of ugly numbers until we have iterated n times
        # The first ugly number is 1
        for i in range(n - 1):
            # The next ugly number comes from the head of the priority queue
            curr = heapq.heappop(pq)

            # Generate new ugly numbers and add them to the priority queue
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(pq, nxt)

        # Return the result
        return heapq.heappop(pq)