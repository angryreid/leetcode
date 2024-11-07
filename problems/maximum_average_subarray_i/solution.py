class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr = float('-inf')
        sums = 0
        left = 0
        for right in range(len(nums)):
            sums += nums[right]
            if right - left + 1 == k:
                max_avr = max(max_avr, sums / k)
            if right >= k - 1:
                sums -= nums[left]
                left += 1
        return max_avr
