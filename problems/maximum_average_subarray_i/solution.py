class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = cur = sum(nums[:k])
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]
            if cur > best:
                best = cur
        return best / k
