class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        sums = 0
        max_value = float('-inf')
        for right in range(len(nums)):
            sums += nums[right]
            if right - left + 1 == k:
                max_value = max(max_value, sums / k)
            if right >= k - 1:
                sums -= nums[left]
                left += 1
            right += 1
        return max_value