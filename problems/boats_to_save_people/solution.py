class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        n = len(people)
        left, right = 0, n - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                ans += 1
                right -= 1
        return ans

        