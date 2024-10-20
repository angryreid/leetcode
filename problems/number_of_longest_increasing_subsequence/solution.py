class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n

        max_len = 1

        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[i] == dp[j] + 1:
                    cnt[i] += cnt[j]
            max_len = max(max_len, dp[i])
        res = 0

        for i in range(n):
            if dp[i] == max_len:
                res += cnt[i]
        return res