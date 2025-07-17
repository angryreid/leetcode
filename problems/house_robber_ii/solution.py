class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        res = dp[-1]
        dp = [0] * (n - 1)
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], nums[i + 1] + dp[i - 2])
        return max(res, dp[-1])